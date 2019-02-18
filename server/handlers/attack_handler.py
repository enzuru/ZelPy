from handlers.handler import Handler


class AttackHandler(Handler):

    def execute(self):
        self.sender.character.attack()
