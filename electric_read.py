from dataclasses import dataclass
from datetime import datetime


@dataclass
class ElectricRead:
    time: datetime
    id: int
    voltage: float
    kwh: float
