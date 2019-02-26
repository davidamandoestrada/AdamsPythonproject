import logging
import smirnov_grubbs as grubbs

from matplotlib import pyplot
from pandas import DataFrame, read_csv
import numpy as np


class Frames:
    def __init__(self, reads=[]):
        self._frames = {}
        self._ids = []
        self._current_id_index = 0

        for read in reads:
            self.add(read)

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_id_index >= len(self._ids):
            self._current_id_index = 0
            raise StopIteration
        else:
            self._current_id_index += 1
            return self._ids[self._current_id_index - 1]

    def add(self, read):
        if read.id not in self.frames:
            self.frames[read.id] = {"Time": [], "Voltage": [], "KWH": []}
            self._ids.append(read.id)
        self.frames[read.id]["Time"].append(read.time)
        self.frames[read.id]["Voltage"].append(read.voltage)
        self.frames[read.id]["KWH"].append(read.kwh)

    @property
    def frames(self):
        return self._frames

    def get_frame_by_id(self, id: str):
        if id in self.frames:
            return self.frames[id]
        else:
            raise LookupError

    def get_time_sorted_frame_by_id(self, id: str):
        frame = self.get_frame_by_id(id)
        return self._sort_voltage_and_kwh_by_time(frame)

    def add_frame_to_plot_by_id(self, id):
        df = DataFrame(data=self.get_time_sorted_frame_by_id(id))
        logging.info(f"Add frame with ID {id} to plot")
        pyplot.plot(df["Time"], df["Voltage"])

    def show_plots(self):
        pyplot.show()

    def _sort_voltage_and_kwh_by_time(self, dictionary_of_time_voltage_kwh):
        sorted_dictionary = {}
        sorted_dictionary["Time"], sorted_dictionary["Voltage"], sorted_dictionary["KWH"] = zip(
            *sorted(zip(dictionary_of_time_voltage_kwh["Time"], dictionary_of_time_voltage_kwh["Voltage"], dictionary_of_time_voltage_kwh["KWH"])))
        return sorted_dictionary
    
    # This takes all the voltage reads and makes a numPy array. I assume the data is all sorted in time
    def build_voltage_np_array(self):
        voltage_matrix = []
        for id in self.frames:
            #print(self.frames[id]["Voltage"])
            voltage_matrix.append(self.frames[id]["Voltage"])
        return np.array(voltage_matrix)
    
    #Not done yet, need to take all the outliers found for each time slice to decide
    #which device(s) is the outlier, if any
    def get_outliers(self):
        outliers = []
        voltage_np_array = self.build_voltage_np_array() 
        # Get outliers of voltages at each time / column, so iterate thru the columns
        # Thus iterate thru the transpose   
        for col in voltage_np_array.T:
            outliers.append(grubbs.min_test_indices(col, alpha=0.05))
        return outliers
            
