from flask import jsonify
from flask_restful import Resource, abort
from server_service import *


# returns a list of all servers
class ServerLister(Resource):

    def get(self):
        return jsonify([servers[key].serialize() for key in servers])


# returns details of a single server and manages it's status
class ServerManager(Resource):

    def get(self, server_id):
        response = get_server_details(server_id)

        if response:
            return jsonify(response.serialize())
        else:
            abort(404, error="Server with ID {} does not exist.".format(server_id))

    def put(self, server_id):
        return 'this will check out a server or deny the request if that server is already checked out or down'
