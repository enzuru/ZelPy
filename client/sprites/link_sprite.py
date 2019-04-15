import uuid
from typing import Any
from typing import Optional

from sprites.sprite import Sprite

class LinkSprite(Sprite):
    def __init__(
        self,
        uuid: str = uuid.uuid4(),
        x: int = 0,
        y: int = 0,
        action: str = "standing",
        direction: str = "down",
        index: int = 0,
        parent: Optional[Any] = None,
    ):
        self.actions = ["standing", "walking", "attacking"]
        self.directions = ["up", "down", "left", "right"]
        super().__init__(uuid, x, y, action, direction, index, parent)
        self.set_image(self.images[self.action][self.direction][self.index])

    def update(self) -> None:
        images = self.images[self.action][self.direction]
        self.index += 1
        if self.index >= len(images):
            self.index = 0
            self.action = "standing"
        self.set_image(images[self.index])

    def attack(self) -> None:
        self.index = 0
        self.action = "attacking"

    def move(self, x: int, y: int) -> None:
        if self.action == "attacking":
            return

        if self.x != x or self.y != y:
            self.action = "walking"
        else:
            self.action = "standing"

        if self.x > x:
            self.direction = "left"
        elif self.x < x:
            self.direction = "right"

        if self.y > y:
            self.direction = "up"
        elif self.y < y:
            self.direction = "down"

        self.x = x
        self.y = y
