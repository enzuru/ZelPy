from handlers.handler import Handler
from handlers.up_handler import UpHandler
from handlers.down_handler import DownHandler
from handlers.left_handler import LeftHandler
from handlers.right_handler import RightHandler
from handlers.attack_handler import AttackHandler


class ButtonsPressedHandler(Handler):

    button_types = {
        "up": UpHandler,
        "down": DownHandler,
        "left": LeftHandler,
        "right": RightHandler,
        "a": AttackHandler
    }

    def execute(self):
        buttons = self.value['buttons']
        for button in buttons:
            if button in self.button_types:
                self.button_types[button](self.sender, None).execute()
