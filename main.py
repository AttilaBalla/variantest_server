from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
# app.secret_key = 'You would never guess it!'
api = Api(app)


# just to test if it's alive
class HelloWorld(Resource):
    def get(self):
        return 'Hello, I\'m alive and working!'


# returns a list of all servers
class ServerLister(Resource):

    def get(self):
        return 'hello, Im going to display all servers here'


# returns details of a single server and manages it's status
class ServerManager(Resource):

    def get(self, server_id):
        return 'hello, Im going to display details of one server'


api.add_resource(ServerManager, '/server/<int:server_id>')
api.add_resource(ServerLister, '/servers')
api.add_resource(HelloWorld, '/')

if __name__ == "__main__":
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )
