from sprites.link_sprite import LinkSprite


class SpriteFactory():

    @classmethod
    def create(cls, obj):
        type = obj['type']
        uuid = obj['value']['uuid']
        x = obj['value']['x']
        y = obj['value']['y']
        if type == 'link':
            return LinkSprite(uuid, x, y)
        else:
            return None
