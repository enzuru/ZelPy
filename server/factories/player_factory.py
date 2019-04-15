from typing import Tuple

from directories.player_directory import PlayerDirectory
from participants.player import Player

class PlayerFactory:
    @classmethod
    def create(cls, username: str, ip: str, port: int) -> Player:
        player = Player(username, ip, port, True)
        PlayerDirectory.add(player)
        return player

    @classmethod
    def assign_birthplace(cls) -> Tuple[int, int]:
        return (0, 0)
