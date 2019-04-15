from typing import Any
from typing import Dict

from messages.message import Message

class RequestToJoin(Message):
    def __init__(self, username: str, port: int):
        self.username = username
        self.port = port

    def message(self) -> Dict[str, Any]:
        return {
            "sender": self.username,
            "messages": [{"type": "request_to_join", "value": {"port": self.port}}],
        }
