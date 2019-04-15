from typing import Tuple

from characters.link import Link
from participants.participant import Participant

class Player(Participant):
    def __init__(
        self,
        username: str,
        ip: str,
        port: int,
        create_character: bool = False,
        birthplace: Tuple[int, int] = (0, 0),
    ) -> None:
        self.username = username
        self.ip = ip
        self.port = port
        x, y = birthplace
        if create_character:
            self.character = Link(x, y)
