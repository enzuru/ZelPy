import pygame
from pygame import sprite
from sprites.sprite import Sprite
import uuid


class LinkSprite(Sprite):

    def __init__(self, uuid=uuid.uuid4(), x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.uuid = uuid
        self.x = x
        self.y = y
        self.width = 64
        self.height = 64

        self.images = []
        self.images.append(pygame.image.load('images/down2.png'))
        self.images.append(pygame.image.load('images/down3.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.mask = pygame.mask.from_surface(self.image)
