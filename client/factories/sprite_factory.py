from sprites.link_sprite import LinkSprite
from sprites.circle_sprite import CircleSprite


class SpriteFactory():

    @classmethod
    def create(cls, obj):
        typ = obj['type']
        uuid = obj['value']['uuid']
        x = obj['value']['x']
        y = obj['value']['y']
        if typ == 'Link':
            return LinkSprite(uuid, x, y)
        elif typ == 'Circle':
            return CircleSprite(uuid, x, y)
        else:
            return None
