import pygame
from pygame import sprite
import uuid


class Sprite(sprite.Sprite):

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

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
        if self.x < x:
            self.direction = 'right'
        if self.y > y:
            self.direction = 'up'
        if self.y < y:
            self.direction = 'down'
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
