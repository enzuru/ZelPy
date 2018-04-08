from participants.player import Player


class PlayerFactory:

    @classmethod
    def create(cls, username, ip, port):
        player = Player(username, ip, port)
        return player

    @classmethod
    def assign_birthplace(cls):
        return (0, 0)
