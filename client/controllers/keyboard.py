import pygame


class Keyboard:

    def get_buttons_pressed(self):
        buttons = []
        keys = pygame.key.get_pressed()
        print(keys)
        if keys[pygame.K_LEFT]:
            buttons.append('left')
        if keys[pygame.K_RIGHT]:
            buttons.append('right')
        if keys[pygame.K_UP]:
            buttons.append('up')
        if keys[pygame.K_DOWN]:
            buttons.append('down')
        return buttons