import pygame
from directories.sprite_directory import SpriteDirectory
from services.colors import Colors

class Window:
    def __init__(self) -> None:
        pygame.init()
        pygame.joystick.init()
        self.done = False
        self.clock = pygame.time.Clock()
        self.refresh_rate = 60
        self.size = [455, 256]
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("ZelPy")

    def check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

    def update(self) -> None:
        self.screen.fill(Colors.grass)
        SpriteDirectory.sprite_group.update()
        SpriteDirectory.sprite_group.draw(self.screen)
        pygame.display.flip()
        self.clock.tick(self.refresh_rate)

    def quit(self) -> None:
        pygame.quit()
