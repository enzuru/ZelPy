import pygame

class SpriteDirectory:

    sprites_by_uuid = {}
    sprite_group = pygame.sprite.Group()

    @classmethod
    def add_sprite(cls, sprite):
        SpriteDirectory.sprites_by_uuid[sprite.uuid] = sprite
        SpriteDirectory.sprite_group.add(sprite)

    @classmethod
    def lookup_sprite(cls, uuid):
        if uuid in SpriteDirectory.sprites_by_uuid:
            return SpriteDirectory.sprites_by_uuid[uuid]
        else:
            return None
