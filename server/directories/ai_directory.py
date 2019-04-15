from typing import Dict
from typing import Optional

from characters.character import Character

class AIDirectory:

    ai_by_uuid: Dict[str, Character] = {}

    @classmethod
    def make_moves(cls) -> None:
        for uuid in cls.ai_by_uuid:
            cls.ai_by_uuid[uuid].update()

    @classmethod
    def add(cls, ai: Character) -> None:
        AIDirectory.ai_by_uuid[ai.uuid] = ai

    @classmethod
    def lookup(cls, uuid: str) -> Optional[Character]:
        if uuid in AIDirectory.ai_by_uuid:
            return AIDirectory.ai_by_uuid[uuid]
        else:
            return None

    @classmethod
    def remove(cls, uuid: str) -> None:
        AIDirectory.ai_by_uuid.pop(uuid, None)
