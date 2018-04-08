from handlers.handler import Handler


class RightHandler(Handler):

    def execute(self):
        self.sender.character.right()
