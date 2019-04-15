import uuid

from characters.character import Character
from directories.server_directory import ServerDirectory
from directories.sprite_directory import SpriteDirectory
from factories.sprite_factory import SpriteFactory

class Triforce(Character):
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.uuid = str(uuid.uuid4())
        self.x = x
        self.y = y
        self.sprite = SpriteFactory.create(
            {
                "type": "Triforce",
                "value": {
                    "uuid": self.uuid,
                    "x": self.x,
                    "y": self.y,
                    "action": "standard",
                    "direction": "down",
                    "index": 0,
                },
            }
        )
        self.direction = None
        self.sprite.parent = self
        ServerDirectory.add(self)
        SpriteDirectory.add(self.sprite)
