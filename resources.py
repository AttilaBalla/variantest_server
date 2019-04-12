from flask import jsonify
from flask_restful import Resource, abort
from server_service import *
from utilities import *


# returns a list of all servers
class ServerLister(Resource):

    def get(self):
        return jsonify([servers[key].serialize() for key in servers])


# returns details of a single server
class Server(Resource):

    def get(self, server_id):
        server = get_server_details(server_id)

        if server:
            return jsonify(server.serialize())
        else:
            abort(404, error="Server with ID {} does not exist.".format(server_id))

    def put(self, server_id=None):

        if server_id is None:
            server = checkout_first_server()

            if server is None:
                abort(400, error=SERVER_NO_AVAILABLE)
            else:
                return jsonify({"message": message_successful(server)})
        else:
            server = get_server_details(server_id)

            if server is None:
                abort(404, error=SERVER_NOT_FOUND)
            if server.status == ServerStatus.DOWN:
                abort(400, error=SERVER_DOWN)

            checkout_or_release(server)

            return jsonify({"message": message_successful(server)})
