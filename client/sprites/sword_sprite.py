import pygame
from pygame import sprite
#from directories.server_directory import ServerDirectory
from directories.sprite_directory import SpriteDirectory
from sprites.sprite import Sprite
import uuid


class SwordSprite(Sprite):

    def __init__(self, uuid=uuid.uuid4(), x=0, y=0, action='slashing', direction='down', index=0, parent=None):
        self.actions = ['slashing']
        self.directions = ['up', 'down', 'left', 'right']
        super().__init__(uuid, x, y, action, direction, index)
        self.parent = parent
        self.set_image(self.images[self.action][self.direction][self.index])

    def update(self):
        images = self.images[self.action][self.direction]
        self.index += 1
        if self.index >= len(images):
            self.index = 0
            SpriteDirectory.remove(self.uuid)
            if self.parent is not None:
                self.parent.delete()
        self.set_image(images[self.index])
