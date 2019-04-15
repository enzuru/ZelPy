from typing import List

import pygame

class ControllerSNES:
    def __init__(self, ident: int) -> None:
        pygame.joystick.init()
        joysticks = [
            pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())
        ]
        self.joystick = joysticks[int(ident)]
        self.joystick.init()

    def get_buttons_pressed(self) -> List[str]:
        buttons = []
        # for i in range(self.joystick.get_numbuttons()):
        # button = self.joystick.get_button(i)
        if self.joystick.get_button(0):
            buttons.append("a")
        if self.joystick.get_axis(0) < -0.9:
            buttons.append("left")
        if self.joystick.get_axis(0) > 0.9:
            buttons.append("right")
        if self.joystick.get_axis(1) < -0.9:
            buttons.append("up")
        if self.joystick.get_axis(1) > 0.9:
            buttons.append("down")
        return buttons
