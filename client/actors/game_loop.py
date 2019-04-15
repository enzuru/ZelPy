import importlib
from typing import Any
from typing import Dict

import pykka
from messengers.messenger_for_client import MessengerForClient
from services.game import Game
from services.window import Window

class GameLoop(pykka.ThreadingActor):
    def __init__(
        self, username: str, ip: str, controller_id: int, controller_type: str
    ) -> None:
        super(GameLoop, self).__init__()
        self.username = username
        self.messenger = MessengerForClient(ip)
        self.window = Window()
        self.setup_controller(controller_id, controller_type)

    def setup_controller(self, controller_id: int, controller_type: str) -> None:
        class_name = "Controller" + controller_type.upper()
        mod = importlib.import_module("controllers.controller_" + controller_type)
        Controller = getattr(mod, class_name)
        self.controller = Controller(controller_id)

    def on_receive(self, message: Dict[Any, Any]) -> bool:
        self.window.check_events()
        self.messenger.get_messages()
        buttons = self.controller.get_buttons_pressed()

        if self.window.done == True:
            self.window.quit()
        elif Game.joined == False:
            self.messenger.request_to_join_game(self.username)
        elif len(buttons) > 0:
            self.messenger.send_buttons_pressed(self.username, buttons)

        self.window.update()
        return True
