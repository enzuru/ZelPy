from handlers.handler import Handler

class UpHandler(Handler):
    def execute(self) -> None:
        self.sender.character.up()
