import uuid

from characters.character import Character
from characters.link import Link
from directories.ai_directory import AIDirectory
from directories.server_directory import ServerDirectory
from directories.sprite_directory import SpriteDirectory
from factories.sprite_factory import SpriteFactory

class Poe(Character):
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.uuid = str(uuid.uuid4())
        self.x = x
        self.y = y
        self.sprite = SpriteFactory.create(
            {
                "type": "Poe",
                "value": {
                    "uuid": self.uuid,
                    "x": self.x,
                    "y": self.y,
                    "action": "walking",
                    "direction": "left",
                    "index": 0,
                },
            }
        )
        self.direction = None
        self.sprite.parent = self
        SpriteDirectory.add(self.sprite)
        ServerDirectory.add(self)
        AIDirectory.add(self)

    def update(self) -> None:
        for uuid in SpriteDirectory.sprites_by_uuid:
            sprite = SpriteDirectory.sprites_by_uuid[uuid]
            if type(sprite.parent) is Link:
                if sprite.parent.x > self.x:
                    self.x = self.x + 1
                if sprite.parent.x < self.x:
                    self.x = self.x - 1
                if sprite.parent.y > self.y:
                    self.y = self.y + 1
                if sprite.parent.y < self.y:
                    self.y = self.y - 1
                break
