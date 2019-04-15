from typing import Dict
from typing import Optional

from characters.character import Character

class ServerDirectory:

    objects_by_uuid: Dict[str, Character] = {}

    @classmethod
    def add(cls, obj: Character) -> None:
        ServerDirectory.objects_by_uuid[obj.uuid] = obj

    @classmethod
    def remove(cls, uuid: str) -> None:
        ServerDirectory.objects_by_uuid.pop(uuid, None)

    @classmethod
    def lookup(cls, uuid: str) -> Optional[Character]:
        if uuid in ServerDirectory.objects_by_uuid:
            return ServerDirectory.objects_by_uuid[uuid]
        else:
            return None
