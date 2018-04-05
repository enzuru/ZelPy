import uuid

class Link:

    def __init__(self, x = 0, y = 0):
        self.uuid = str(uuid.uuid4())
        self.x = x
        self.y = y

    def right(self):
        self.x = self.x + 1

    def left(self):
        self.x = self.x - 1

    def up(self):
        self.y = self.y - 1

    def down(self):
        self.y = self.y + 1
