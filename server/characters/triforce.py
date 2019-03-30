import uuid
from directories.sprite_directory import SpriteDirectory
from directories.server_directory import ServerDirectory
from factories.sprite_factory import SpriteFactory
from characters.character import Character


class Triforce(Character):

    def __init__(self, x=0, y=0):
        self.uuid = str(uuid.uuid4())
        self.x = x
        self.y = y
        self.sprite = SpriteFactory.create({
            'type': 'Triforce',
            'value': {
                'uuid': self.uuid,
                'x': self.x,
                'y': self.y,
                'action': 'standard',
                'direction': 'down',
                'index': 0
            }
        })
        self.direction = None
        ServerDirectory.add(self)
        SpriteDirectory.add(self.sprite)
