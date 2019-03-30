import pygame
from services.colors import Colors
from directories.sprite_directory import SpriteDirectory


class Surface:

    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.done = False
        self.clock = pygame.time.Clock()
        self.refresh_rate = 60
        self.size = [455, 256]
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("ZelPy")

    def update(self):
        self.screen.fill(Colors.grass)
        SpriteDirectory.sprite_group.update()
        SpriteDirectory.sprite_group.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(self.refresh_rate)
