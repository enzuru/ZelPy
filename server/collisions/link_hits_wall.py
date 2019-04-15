from characters.character import Character
from collisions.collision import Collision

class LinkHitsWall(Collision):
    def execute(link: Character, wall: Character) -> None:
        self.x = self.x
        self.y = self.y
