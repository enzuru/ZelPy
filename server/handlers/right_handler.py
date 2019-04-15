from handlers.handler import Handler

class RightHandler(Handler):
    def execute(self) -> None:
        self.sender.character.right()
