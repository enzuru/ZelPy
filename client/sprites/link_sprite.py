import pygame
from pygame import sprite
from sprites.sprite import Sprite
import uuid


class LinkSprite(Sprite):

    def __init__(self, uuid=uuid.uuid4(), x=0, y=0, action='standing', direction='down', index=0):
        self.actions = ['standing', 'walking', 'attacking']
        self.directions = ['up', 'down', 'left', 'right']
        super().__init__(uuid, x, y, action, direction, index)
        self.set_image(self.images[self.action][self.direction][self.index])

    def update(self):
        images = self.images[self.action][self.direction]
        self.index += 1
        if self.index >= len(images):
            self.index = 0
            self.action = 'standing'
        self.set_image(images[self.index])

    def attack(self):
        self.index = 0
        self.action = 'attacking'

    def move(self, x, y):
        if self.action == 'attacking':
            return

        if self.x != x or self.y != y:
            self.action = 'walking'
        else:
            self.action = 'standing'

        if self.x > x:
            self.direction = 'left'
        elif self.x < x:
            self.direction = 'right'

        if self.y > y:
            self.direction = 'up'
        elif self.y < y:
            self.direction = 'down'

        self.x = x
        self.y = y
