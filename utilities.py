import random
from enum import Enum


# defines possible statuses for a server
class ServerStatus(Enum):
    DOWN = "Down"
    AVAILABLE = "Available"
    CHECKED_OUT = "Checked Out"


# sets server status with a 30% chance of a server being down
def setServerStatus():
    if (random.randint(0, 10)):
        return ServerStatus.AVAILABLE
    else:
        return ServerStatus.DOWN


# --------- messages -----------

SERVER_NOT_FOUND = "Server with that ID could not be found"
SERVER_ID_INVALID = "Invalid server ID. It has to be a positive int"
SERVER_DOWN = "Cannot perform operation: Server is down."
SERVER_NO_AVAILABLE = "No available servers left to check out."


def message_successful(server):
    return "Server ID '{}' is now {}".format(server.id, server.status.value)
