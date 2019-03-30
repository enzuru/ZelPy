import uuid
from directories.server_directory import ServerDirectory
from directories.sprite_directory import SpriteDirectory
from factories.sprite_factory import SpriteFactory
from characters.character import Character


class Sword:

    def __init__(self, x=0, y=0, direction='down'):
        self.uuid = str(uuid.uuid4())
        self.x = x
        self.y = y
        self.sprite = SpriteFactory.create({
            'type': 'Sword',
            'value': {
                'uuid': self.uuid,
                'x': self.x,
                'y': self.y,
                'action': 'slashing',
                'direction': direction,
                'index': 0
            }
        })
        self.sprite.parent = self
        ServerDirectory.add(self)
        SpriteDirectory.add(self.sprite)

    def delete(self):
        ServerDirectory.remove(self.uuid)
