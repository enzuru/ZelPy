from typing import Any

class Handler:
    def __init__(self, sender: Any, value: Any) -> None:
        self.sender = sender
        self.value = value
