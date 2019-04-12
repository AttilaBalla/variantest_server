from flask import Flask, request
from flask_restful import Resource, Api
from resources import Server, ServerLister
import server_service


app = Flask(__name__)
api = Api(app)

# initialize n number of servers
server_service.initialize(10)

api.add_resource(Server, '/server', '/server/<int:server_id>')
api.add_resource(ServerLister, '/servers', '/')

if __name__ == "__main__":
    app.run(
        debug=True,  # Allow verbose error reports
        port=5000  # Set custom port
    )
