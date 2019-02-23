# %%
from pandas import read_csv

from config import FAKE_VOLTAGE_DATA_PATH
from electric_read import ElectricRead
from frames import Frames

rows = read_csv(FAKE_VOLTAGE_DATA_PATH)
electric_reads = [ElectricRead(time=row["Time"], id=row["ID"],
                               voltage=row["Voltage"], kwh=row["KWH"]) for index, row in rows.iterrows()]

frames = Frames(electric_reads)

for id in frames:
    frames.add_frame_to_plot_by_id(id)

frames.show_plots()
