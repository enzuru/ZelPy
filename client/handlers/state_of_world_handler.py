from handlers.handler import Handler
from directories.sprite_directory import SpriteDirectory
from factories.sprite_factory import SpriteFactory
from services.game import Game


class StateOfWorldHandler(Handler):

    def execute(self):
        Game.joined = True
        for obj in self.value['objects']:
            uuid = obj['value']['uuid']
            x = obj['value']['x']
            y = obj['value']['y']
            action = obj['value']['action']
            sprite = SpriteDirectory.lookup_sprite(uuid)
            if sprite:
                sprite.move(x, y)
                if action == 'attacking':
                    sprite.attack()
            else:
                sprite = SpriteFactory.create(obj)
                SpriteDirectory.add_sprite(sprite)
