from typing import Any
from typing import Dict
from typing import List

from messages.message import Message

class ButtonsPressed(Message):
    def __init__(self, username: str, buttons: List[str]) -> None:
        self.username = username
        self.buttons = buttons

    def message(self) -> Dict[str, Any]:
        return {
            "sender": self.username,
            "messages": [
                {"type": "buttons_pressed", "value": {"buttons": self.buttons}}
            ],
        }
