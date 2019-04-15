import json
from typing import Any

from pymemcache.client.base import Client

from directories.player_directory import PlayerDirectory

class WorldCache:

    KEY = "world"

    def __init__(self) -> None:
        self.client = Client(
            ("localhost", 11211),
            serializer=self.json_serializer,
            deserializer=self.json_deserializer,
        )

    def json_serializer(self, key: Any, value: Any) -> Any:
        if type(value) == str:
            return value, 1
        return json.dumps(value), 2

    def json_deserializer(self, key: Any, value: Any, flags: int) -> Any:
        if flags == 1:
            return value
        if flags == 2:
            return json.loads(value.decode())

    def save(self) -> None:
        state = {"players": PlayerDirectory.players_by_username}
        self.client.set(self.KEY, state)

    def load(self) -> None:
        print("Loading cache...")
        value = self.client.get(self.KEY)
        print(value)
