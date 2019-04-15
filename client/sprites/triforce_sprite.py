import uuid
from typing import Any
from typing import Optional

import pygame
from sprites.sprite import Sprite

class TriforceSprite(Sprite):
    def __init__(
        self,
        uuid: str = uuid.uuid4(),
        x: int = 0,
        y: int = 0,
        action: str = "standard",
        direction: str = "down",
        index: int = 0,
        parent: Optional[Any] = None,
    ) -> None:
        super().__init__(uuid, x, y, action, direction, index, parent)

    def load_images(self) -> None:
        self.images = []
        self.images.append(pygame.image.load("images/link-triforce.png"))
        self.image = self.images[self.index]
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self) -> None:
        self.x = self.x
        self.y = self.y
