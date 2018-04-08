from handlers.handler import Handler


class DownHandler(Handler):

    def execute(self):
        self.sender.character.down()
