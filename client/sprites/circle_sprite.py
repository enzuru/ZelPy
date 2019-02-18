import pygame
from pygame import sprite
from sprites.sprite import Sprite
import uuid


class CircleSprite(Sprite):

    def __init__(self, uuid=uuid.uuid4(), x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.uuid = uuid
        self.x = x
        self.y = y
        self.width = 140
        self.height = 260
        self.action = 'standard'

        self.images = []
        self.images.append(pygame.image.load('images/link-triforce.png'))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.mask = pygame.mask.from_surface(self.image)
