# %%
import logging

from matplotlib import pyplot
from pandas import DataFrame, read_csv

from config import FAKE_VOLTAGE_DATA_PATH
from electric_read import ElectricRead
from utility import sort_voltage_and_kwh_by_time

rows = read_csv(FAKE_VOLTAGE_DATA_PATH)
electric_reads = [ElectricRead(time=row["Time"], id=row["ID"],
                               voltage=row["Voltage"], kwh=row["KWH"]) for index, row in rows.iterrows()]

frames = {}
for read in electric_reads:
    if read.id not in frames:
        frames[read.id] = {"Time": [], "Voltage": [], "KWH": []}
    frames[read.id]["Time"].append(read.time)
    frames[read.id]["Voltage"].append(read.voltage)
    frames[read.id]["KWH"].append(read.kwh)

for id in frames:
    df = DataFrame(data=sort_voltage_and_kwh_by_time(frames.get(id)))
    logging.info(f"New dataframe for ID {id}")
    pyplot.plot(df["Time"], df["Voltage"])

pyplot.show()
