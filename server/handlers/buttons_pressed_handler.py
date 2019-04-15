from typing import Dict

from handlers.attack_handler import AttackHandler
from handlers.down_handler import DownHandler
from handlers.handler import Handler
from handlers.left_handler import LeftHandler
from handlers.right_handler import RightHandler
from handlers.up_handler import UpHandler


class ButtonsPressedHandler(Handler):

    button_types: Dict[str, Handler] = {
        "up": UpHandler,
        "down": DownHandler,
        "left": LeftHandler,
        "right": RightHandler,
        "a": AttackHandler,
    }

    def execute(self) -> None:
        buttons = self.value["buttons"]
        for button in buttons:
            if button in self.button_types:
                self.button_types[button](self.sender, None).execute()
