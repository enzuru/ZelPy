from typing import List

import pygame

class ControllerKB:
    def __init__(self, ident: int) -> None:
        self.ident = ident

    def get_buttons_pressed(self) -> List[str]:
        buttons = []
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            buttons.append("left")
        if keys[pygame.K_RIGHT]:
            buttons.append("right")
        if keys[pygame.K_UP]:
            buttons.append("up")
        if keys[pygame.K_DOWN]:
            buttons.append("down")
        if keys[pygame.K_SPACE]:
            buttons.append("a")
        return buttons
