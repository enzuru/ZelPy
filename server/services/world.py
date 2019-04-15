from typing import Any
from typing import Dict

from directories.server_directory import ServerDirectory

class World:
    @classmethod
    def load(cls) -> None:
        print("World loaded")

    @classmethod
    def save(cls) -> None:
        print("World saved")

    @classmethod
    def get_state(cls) -> Dict[str, Any]:
        state: Dict[str, Any]
        state = {"objects": []}
        for uuid in ServerDirectory.objects_by_uuid:
            obj = ServerDirectory.objects_by_uuid[uuid]
            state["objects"].append(
                {
                    "type": type(obj).__name__,
                    "value": {
                        "uuid": uuid,
                        "x": obj.x,
                        "y": obj.y,
                        "action": obj.sprite.action,
                        "direction": obj.sprite.direction,
                        "index": obj.sprite.index,
                    },
                }
            )
        return state
