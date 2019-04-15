from handlers.handler import Handler

class LeftHandler(Handler):
    def execute(self) -> None:
        self.sender.character.left()
