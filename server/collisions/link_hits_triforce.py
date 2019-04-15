from characters import Character
from collisions.LinkHitsWall import LinkHitsWall

class LinkHitsTriforce(LinkHitsWall):
    def execute(link: Character, triforce: Character) -> None:
        self.x = self.x
        self.y = self.y
