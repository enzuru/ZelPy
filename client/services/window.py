import pygame
from services.colors import Colors
from directories.sprite_directory import SpriteDirectory


class Window:

    def __init__(self):
        pygame.init()
        pygame.joystick.init()
        self.done = False
        self.clock = pygame.time.Clock()
        self.refresh_rate = 60
        self.size = [512, 448]
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("ZelPy")

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

    def update(self):
        self.screen.fill(Colors.white)
        SpriteDirectory.sprite_group.update()
        SpriteDirectory.sprite_group.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(self.refresh_rate)

    def quit(self):
        pygame.quit()
