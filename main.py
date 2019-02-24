# %%
from pandas import read_csv

from config import FAKE_VOLTAGE_DATA_PATH
from electric_read import ElectricRead
from frames import Frames

electric_reads = [ElectricRead(time=row["Time"], id=row["ID"],
                               voltage=row["Voltage"], kwh=row["KWH"]) for index, row
                  in read_csv(filepath_or_buffer=FAKE_VOLTAGE_DATA_PATH).iterrows()]
frames = Frames(reads=electric_reads)

for id in frames:
    frames.add_frame_to_plot_by_id(id=id)

frames.show_plots()
