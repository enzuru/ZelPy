import uuid
from directories.sprite_directory import SpriteDirectory
from factories.sprite_factory import SpriteFactory


class Link:

    def __init__(self, x=0, y=0):
        self.uuid = str(uuid.uuid4())
        self.x = x
        self.y = y
        self.sprite = SpriteFactory.create({
            'type': 'link',
            'value': {
                'uuid': self.uuid,
                'x': self.x,
                'y': self.y
            }
        })
        SpriteDirectory.add_sprite(self.sprite)

    def right(self):
        self.x = self.x + 1

    def left(self):
        self.x = self.x - 1

    def up(self):
        self.y = self.y - 1

    def down(self):
        self.y = self.y + 1
