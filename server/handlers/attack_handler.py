from handlers.handler import Handler

class AttackHandler(Handler):
    def execute(self) -> None:
        self.sender.character.attack()
