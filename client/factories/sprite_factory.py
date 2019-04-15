import importlib
from typing import Any
from typing import Dict

from sprites.sprite import Sprite

class SpriteFactory:
    @classmethod
    def create(cls, obj: Dict[str, Any]) -> Sprite:
        typ = obj["type"]
        uuid = obj["value"]["uuid"]

        x = obj["value"]["x"]
        y = obj["value"]["y"]

        action = obj["value"]["action"]
        direction = obj["value"]["direction"]
        index = obj["value"]["index"]

        mod = importlib.import_module("sprites." + typ.lower() + "_sprite")
        Sprite = getattr(mod, typ + "Sprite")

        return Sprite(uuid, x, y, action, direction, index)
