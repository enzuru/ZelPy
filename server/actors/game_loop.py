from typing import Any
from typing import Dict

import pykka
from cache.world_cache import WorldCache
from characters.triforce import Triforce
from directories.ai_directory import AIDirectory
from messengers.messenger_for_server import MessengerForServer
from services.surface import Surface

class GameLoop(pykka.ThreadingActor):
    def __init__(self, ip: str, port: int) -> None:
        super(GameLoop, self).__init__()
        self.ai = AIDirectory()
        self.messenger = MessengerForServer(ip, port)
        self.cache = WorldCache()
        self.surface = Surface()

        # Poe(200, 200)
        Triforce(300, 300)

    def on_receive(self, message: Dict[Any, Any]) -> bool:
        self.messenger.get_messages()
        self.ai.make_moves()
        self.surface.update()
        self.messenger.update_all_players()
        return True
