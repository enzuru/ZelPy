from typing import Any
from typing import Dict
from typing import Optional

from handlers.buttons_pressed_handler import ButtonsPressedHandler
from handlers.handler import Handler
from handlers.request_to_join_handler import RequestToJoinHandler
from participants.participant import Participant

class InterpreterForServer:

    message_types: Dict[str, Handler] = {
        "request_to_join": RequestToJoinHandler,
        "buttons_pressed": ButtonsPressedHandler,
    }

    def interpret(
        self, sender: Participant, message: Dict[str, Any]
    ) -> Optional[Handler]:
        if message["type"] in self.message_types:
            return self.message_types[message["type"]](sender, message["value"])
        else:
            return None
