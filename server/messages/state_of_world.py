from typing import Any
from typing import Dict

class StateOfWorld:
    def __init__(self, state: Dict[str, Any]) -> None:
        self.state = state

    def message(self) -> Dict[str, Any]:
        return {
            "sender": "server",
            "messages": [{"type": "state_of_world", "value": self.state}],
        }
