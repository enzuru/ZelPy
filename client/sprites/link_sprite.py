import pygame
from pygame import sprite
import uuid

class LinkSprite(sprite.Sprite):

    def __init__(self, uuid = uuid.uuid4(), x = 0, y = 0):
        pygame.sprite.Sprite.__init__(self)
        self.uuid = uuid
        self.x = x
        self.y = y

        self.images = []
        self.images.append(pygame.image.load('images/down2.png'))
        self.images.append(pygame.image.load('images/down3.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(self.x, self.y, 64, 64)

        #return super(sprite.Sprite, self).__init__()

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(self.x, self.y, 64, 64)

    def move(self, x, y):
        self.x = x
        self.y = y
