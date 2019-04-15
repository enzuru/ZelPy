from typing import Dict
from typing import Optional

from participants.player import Player

class PlayerDirectory:

    players_by_username: Dict[str, Player] = {}

    @classmethod
    def add(cls, player: Player) -> None:
        PlayerDirectory.players_by_username[player.username] = player

    @classmethod
    def lookup(cls, username: str) -> Optional[Player]:
        if username in PlayerDirectory.players_by_username:
            return PlayerDirectory.players_by_username[username]
        else:
            return None
