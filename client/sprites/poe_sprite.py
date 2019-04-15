import uuid
from typing import Any
from typing import Optional

from sprites.sprite import Sprite

class PoeSprite(Sprite):
    def __init__(
        self,
        uuid: str = uuid.uuid4(),
        x: int = 0,
        y: int = 0,
        action: str = "walking",
        direction: str = "left",
        index: int = 0,
        parent: Optional[Any] = None,
    ):
        self.actions = ["walking"]
        self.directions = ["left", "right"]
        super().__init__(uuid, x, y, action, direction, index, parent)
        self.set_image(self.images[self.action][self.direction][self.index])
