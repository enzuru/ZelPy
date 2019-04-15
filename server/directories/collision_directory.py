import importlib

from characters.character import Character
from collisions.collision import Collision

class CollisionDirectory:
    @classmethod
    def lookup(cls, obj: Character, sub: Character) -> Collision:
        return
        first = type(obj).__name__
        second = type(sub).__name__

        first = first.replace("Sprite", "")
        second = second.replace("Sprite", "")

        if first == second:
            return

        class_name = first + "Hits" + second
        mod = importlib.import_module(
            "collisions." + first.lower() + "_hits_" + second.lower()
        )
        collision = getattr(mod, class_name)
        return collision
