from typing import Dict
from typing import Optional

from pygame.sprite import Group
from sprites.sprite import Sprite

class SpriteDirectory:

    sprites_by_uuid: Dict[str, Sprite] = {}
    sprite_group = Group()

    @classmethod
    def add(cls, sprite: Sprite) -> None:
        SpriteDirectory.sprites_by_uuid[sprite.uuid] = sprite
        SpriteDirectory.sprite_group.add(sprite)

    @classmethod
    def lookup(cls, uuid: str) -> Optional[Sprite]:
        if uuid in SpriteDirectory.sprites_by_uuid:
            return SpriteDirectory.sprites_by_uuid[uuid]
        else:
            return None

    @classmethod
    def remove(cls, uuid: str) -> None:
        sprite = SpriteDirectory.lookup(uuid)
        SpriteDirectory.sprite_group.remove(sprite)
        SpriteDirectory.sprites_by_uuid.pop(uuid, None)
