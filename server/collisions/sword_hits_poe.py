from characters import Character
from collisions.collision import Collision

class SwordHitsPoe(Collision):
    def execute(sword: Character, poe: Character) -> None:
        if poe.parent is None:
            return

        if self.direction == "left":
            poe.parent.move_difference(-10, 0)
        elif self.direction == "right":
            poe.parent.move_difference(10, 0)
        elif self.direction == "bottom":
            poe.parent.move_difference(0, 10)
        elif self.direction == "top":
            poe.parent.move_difference(0, -10)
