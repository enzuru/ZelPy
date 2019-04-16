from sprites.sprite import Sprite

class Character:
    def __init__(self, sprite: Sprite) -> None:
        self.sprite = sprite

    def move(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y
        self.sprite.move(self.x, self.y)

    def move_difference(self, x: int = 0, y: int = 0) -> None:
        self.move(self.x + x, self.y + y)

    def right(self) -> None:
        self.move(self.x + 1, self.y)

    def left(self) -> None:
        self.move(self.x - 1, self.y)

    def up(self) -> None:
        self.move(self.x, self.y - 1)

    def down(self) -> None:
        self.move(self.x, self.y + 1)
