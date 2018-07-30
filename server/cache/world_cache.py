import json
from directories.player_directory import PlayerDirectory
from pymemcache.client.base import Client


class WorldCache:

    KEY = 'world'

    def __init__(self):
        self.client = Client(
            ('localhost', 11211),
            serializer=self.json_serializer,
            deserializer=self.json_deserializer
        )

    def json_serializer(self, key, value):
        if type(value) == str:
            return value, 1
        return json.dumps(value), 2

    def json_deserializer(self, key, value, flags):
        if flags == 1:
            return value
        if flags == 2:
            return json.loads(value.decode())

    def save(self):
        state = {
            'players': PlayerDirectory.players_by_username
        }
        self.client.set(self.KEY, state)

    def load(self):
        print("Loading cache...")
        value = self.client.get(self.KEY)
        print(value)
