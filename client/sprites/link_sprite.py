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

        self.load_images()
        self.action = 'standing'
        self.direction = 'down'
        self.index = 0

        self.image = self.images[self.action][self.direction][self.index]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.mask = pygame.mask.from_surface(self.image)

    def load_images(self):
        self.images = {}
        for action in ['standing', 'walking', 'attacking']:
            self.images[action] = {}
            for direction in ['up', 'down', 'left', 'right']:
                self.images[action][direction] = []
                for index in [1, 2, 3, 4, 5, 6, 7, 8]:
                    try:
                        image = 'images/link/' + action + '/' + direction + '/' + str(index) + '.png'
                        self.images[action][direction].append(
                            pygame.image.load(image)
                        )
                    except:
                        print("Doesn't matter")
                    else:
                        print("Else!")

    def update(self):
        images = self.images[self.action][self.direction]
        self.index += 1
        if self.index >= len(images):
            self.index = 0
            self.action = 'standing'
        self.image = images[self.index]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.mask = pygame.mask.from_surface(self.image)
