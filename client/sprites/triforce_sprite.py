import pygame
from pygame import sprite
from sprites.sprite import Sprite
import uuid


class TriforceSprite(Sprite):

    def __init__(self, uuid=uuid.uuid4(), x=0, y=0, action='standard', direction='down', index=0):
        super().__init__(uuid, x, y, action, direction, index)

    def load_images(self):
        self.images = []
        self.images.append(pygame.image.load('images/link-triforce.png'))
        self.image = self.images[self.index]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.mask = pygame.mask.from_surface(self.image)
