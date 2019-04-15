from directories.sprite_directory import SpriteDirectory
from factories.sprite_factory import SpriteFactory
from handlers.handler import Handler
from services.game import Game

class StateOfWorldHandler(Handler):
    def execute(self) -> None:
        Game.joined = True
        for obj in self.value["objects"]:
            uuid = obj["value"]["uuid"]
            x = obj["value"]["x"]
            y = obj["value"]["y"]
            action = obj["value"]["action"]
            index = obj["value"]["index"]
            direction = obj["value"]["direction"]
            sprite = SpriteDirectory.lookup(uuid)
            if sprite:
                sprite.move(x, y)
                sprite.action = action
                sprite.index = index
                sprite.direction = direction
            else:
                sprite = SpriteFactory.create(obj)
                SpriteDirectory.add(sprite)
