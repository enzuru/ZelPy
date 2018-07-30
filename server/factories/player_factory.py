from participants.player import Player
from directories.player_directory import PlayerDirectory


class PlayerFactory:

    @classmethod
    def create(cls, username, ip, port):
        player = Player(username, ip, port, True)
        PlayerDirectory.add(player)
        return player

    @classmethod
    def assign_birthplace(cls):
        return (0, 0)
