import random
from enum import Enum


class ServerStatus(Enum):
    DOWN = "Down"
    AVAILABLE = "Available"
    CHECKED_OUT = "Checked Out"


# sets server status with a 30% chance of a server being down
def setServerStatus():
    if (random.randint(0, 10) <= 7):
        return ServerStatus.AVAILABLE
    else:
        return ServerStatus.DOWN
