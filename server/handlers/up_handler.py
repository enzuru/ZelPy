from handlers.handler import Handler

class UpHandler(Handler):

    def execute(self):
        self.sender.character.up()
