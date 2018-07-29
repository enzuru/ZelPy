import pygame
from directories.sprite_directory import SpriteDirectory


class Surface:

    def __init__(self):
        self.screen = pygame.Surface((1000, 1000))

    def update(self):
        self.screen.fill((0, 0, 0))
        SpriteDirectory.sprite_group.update()
        SpriteDirectory.sprite_group.draw(self.screen)
