from handlers.handler import Handler

class DownHandler(Handler):
    def execute(self) -> None:
        self.sender.character.down()
