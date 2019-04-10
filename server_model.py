from utilities import setServerStatus


class ServerModel:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.status = setServerStatus()

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "status": self.status.value
        }

    def __str__(self):
        return f'ID: {self.id}, name: {self.name}, status: {self.status}'
