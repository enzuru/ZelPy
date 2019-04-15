import uuid

import pygame
from characters.character import Character
from characters.sword import Sword
from collisions.link_hits_wall import LinkHitsWall
from directories.collision_directory import CollisionDirectory
from directories.server_directory import ServerDirectory
from directories.sprite_directory import SpriteDirectory
from factories.sprite_factory import SpriteFactory

class Link(Character):
    def __init__(self, x: int = 0, y: int = 0) -> None:

        self.uuid = str(uuid.uuid4())
        self.x = x
        self.y = y
        self.sprite = SpriteFactory.create(
            {
                "type": "Link",
                "value": {
                    "uuid": self.uuid,
                    "x": self.x,
                    "y": self.y,
                    "action": "standing",
                    "direction": "down",
                    "index": 0,
                },
            }
        )
        self.sprite.parent = self
        ServerDirectory.add(self)
        SpriteDirectory.add(self.sprite)

    def attack(self) -> None:
        if self.sprite.action != "attacking":
            self.sprite.attack()
            Sword(self.x, self.y, self.sprite.direction)

    def move(self, x: int = 0, y: int = 0) -> None:
        self.sprite.move(x, y)
        collisions = pygame.sprite.spritecollide(
            self.sprite, SpriteDirectory.sprite_group, False, pygame.sprite.collide_mask
        )

        for sprite in collisions:
            collision = CollisionDirectory.lookup(self, sprite)
            if collision:
                collision.execute(self, sprite)
                if isinstance(collision, LinkHitsWall):
                    self.x = x
                    self.y = y
                else:
                    self.sprite.move(self.x, self.y)

        self.x = x
        self.y = y
