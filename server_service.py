from server_model import ServerModel
from utilities import ServerStatus

servers = {}


# creates the given number of servers to work with
# parameter: server_count(int) number of servers to create
def initialize(server_count):

    for i in range(server_count):
        servers[i] = ServerModel(i, "server" + str(i+1))


# returns a server based on ID, returns None if ID is not found
# parameter: server_id(int) ID of the server
def get_server_details(server_id):

    if server_id in servers:
        return servers[server_id]
    else:
        return None


# checks out or releases a server
# parameter: Server(object)
# returns the Server object if successful, None otherwise
def checkout_or_release(server):
    if server.status == ServerStatus.AVAILABLE:
        server.status = ServerStatus.CHECKED_OUT

    elif server.status == ServerStatus.CHECKED_OUT:
        server.status = ServerStatus.AVAILABLE

        return server
    else:

        return None


# tries to check out the first available server
# returns the Server object if successful, None otherwise
def checkout_first_server():
    for key in servers:
        if servers[key].status == ServerStatus.AVAILABLE:
            servers[key].status = ServerStatus.CHECKED_OUT

            return servers[key]

    return None
