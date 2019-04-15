import uuid
from typing import Any
from typing import Optional

import pygame
from directories.collision_directory import CollisionDirectory
from directories.sprite_directory import SpriteDirectory
from sprites.sprite import Sprite

class SwordSprite(Sprite):
    def __init__(
        self,
        uuid: str = uuid.uuid4(),
        x: int = 0,
        y: int = 0,
        action: str = "slashing",
        direction: str = "down",
        index: int = 0,
        parent: Optional[Any] = None,
    ) -> None:
        self.actions = ["slashing"]
        self.directions = ["up", "down", "left", "right"]
        super().__init__(uuid, x, y, action, direction, index, parent)
        self.parent = parent
        self.set_image(self.images[self.action][self.direction][self.index])

    def update(self) -> None:
        images = self.images[self.action][self.direction]
        self.index += 1
        if self.index >= len(images):
            self.index = 0
            SpriteDirectory.remove(self.uuid)
            if self.parent is not None:
                self.parent.delete()
        self.set_image(images[self.index])

        collisions = pygame.sprite.spritecollide(
            self, SpriteDirectory.sprite_group, False, pygame.sprite.collide_mask
        )
        print(collisions)
        for sprite in collisions:
            collision = CollisionDirectory.lookup(self, sprite)
            if collision:
                collision.execute(self, sprite)
