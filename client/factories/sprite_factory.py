import importlib


class SpriteFactory():

    @classmethod
    def create(cls, obj):
        typ = obj['type']
        uuid = obj['value']['uuid']

        x = obj['value']['x']
        y = obj['value']['y']

        action = obj['value']['action']
        direction = obj['value']['direction']
        index = obj['value']['index']

        class_name = 'sprites.' + typ + 'Sprite'
        mod = importlib.import_module('sprites.' + typ.lower() + '_sprite')
        Sprite = getattr(mod, typ + 'Sprite')

        return Sprite(uuid, x, y, action, direction, index)
