import uuid
from directories.server_directory import ServerDirectory
from directories.sprite_directory import SpriteDirectory
from factories.sprite_factory import SpriteFactory
from characters.character import Character
from characters.sword import Sword


class Link(Character):

    def __init__(self, x=0, y=0):
        self.uuid = str(uuid.uuid4())
        self.x = x
        self.y = y
        self.sprite = SpriteFactory.create({
            'type': 'Link',
            'value': {
                'uuid': self.uuid,
                'x': self.x,
                'y': self.y,
                'action': 'standing',
                'direction': 'down',
                'index': 0
            }
        })
        ServerDirectory.add(self)
        SpriteDirectory.add(self.sprite)

    def attack(self):
        if self.sprite.action != 'attacking':
            self.sprite.attack()
            Sword(self.x, self.y, self.sprite.direction)
