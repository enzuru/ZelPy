import pygame


class SpriteDirectory:

    sprites_by_uuid = {}
    sprite_group = pygame.sprite.Group()

    @classmethod
    def add(cls, sprite):
        SpriteDirectory.sprites_by_uuid[sprite.uuid] = sprite
        SpriteDirectory.sprite_group.add(sprite)

    @classmethod
    def lookup(cls, uuid):
        if uuid in SpriteDirectory.sprites_by_uuid:
            return SpriteDirectory.sprites_by_uuid[uuid]
        else:
            return None

    @classmethod
    def remove(cls, uuid):
        sprite = SpriteDirectory.lookup(uuid)
        SpriteDirectory.sprite_group.remove(sprite)
        SpriteDirectory.sprites_by_uuid.pop(uuid, None)
