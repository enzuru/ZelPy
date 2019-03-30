import uuid
from directories.ai_directory import AIDirectory
from characters.character import Character
from directories.server_directory import ServerDirectory
from directories.sprite_directory import SpriteDirectory
from factories.sprite_factory import SpriteFactory


class Poe(Character):

    def __init__(self, x=0, y=0):
        self.uuid = str(uuid.uuid4())
        self.x = x
        self.y = y
        self.sprite = SpriteFactory.create({
            'type': 'Poe',
            'value': {
                'uuid': self.uuid,
                'x': self.x,
                'y': self.y,
                'action': 'walking',
                'direction': 'left',
                'index': 0
            }
        })
        self.direction = None
        SpriteDirectory.add(self.sprite)
        ServerDirectory.add(self)
        AIDirectory.add(self)

    def move(self):
        self.x = self.x
        #self.x = self.x+1
        #self.sprite.move(self.x, self.y)
