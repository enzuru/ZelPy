from typing import Any
from typing import Dict
from typing import Optional

from handlers.handler import Handler
from handlers.state_of_world_handler import StateOfWorldHandler
from participants.participant import Participant

class InterpreterForClient:

    message_types = {"state_of_world": StateOfWorldHandler}

    def interpret(
        self, sender: Participant, message: Dict[str, Any]
    ) -> Optional[Handler]:
        if message["type"] in self.message_types:
            return self.message_types[message["type"]](sender, message["value"])
        else:
            return None
