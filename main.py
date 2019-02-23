# %%
import logging

from matplotlib import pyplot
from pandas import DataFrame, read_csv

from config import FAKE_VOLTAGE_DATA_PATH
from electric_read import ElectricRead
from frames import Frames

rows = read_csv(FAKE_VOLTAGE_DATA_PATH)
electric_reads = [ElectricRead(time=row["Time"], id=row["ID"],
                               voltage=row["Voltage"], kwh=row["KWH"]) for index, row in rows.iterrows()]

frames = Frames()
for read in electric_reads:
    frames.add(read)

for id in frames:
    df = DataFrame(data=frames.get_time_sorted_frame_by_id(id))
    logging.info(f"New dataframe for ID {id}")
    pyplot.plot(df["Time"], df["Voltage"])

pyplot.show()
