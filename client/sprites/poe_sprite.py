import pygame
import uuid
from directories.sprite_directory import SpriteDirectory
from pygame import sprite
from sprites.sprite import Sprite


class PoeSprite(Sprite):

    def __init__(self, uuid=uuid.uuid4(), x=0, y=0, action='walking', direction='left', index=0, parent=None):
        self.actions = ['walking']
        self.directions = ['left', 'right']
        super().__init__(uuid, x, y, action, direction, index)
        self.set_image(self.images[self.action][self.direction][self.index])

    def update(self):
        self.x = self.x
        self.y = self.y
