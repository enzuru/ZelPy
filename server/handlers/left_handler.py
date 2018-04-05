from handlers.handler import Handler

class LeftHandler(Handler):

    def execute(self):
        self.sender.character.left()
