from server_model import ServerModel

servers = {}


# creates the given number of servers to work with
def initialize(server_count):

    for i in range(server_count):
        servers[i] = ServerModel(i, "server" + str(i+1))


def get_server_details(server_id):

    if server_id in servers:
        return servers[server_id]
    else:
        return {}
