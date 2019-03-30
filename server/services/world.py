from directories.player_directory import PlayerDirectory
from directories.server_directory import ServerDirectory


class World:

    def load():
        print("World loaded")

    def save():
        print("World saved")

    def get_state():
        state = {"objects": [] }
        for uuid in ServerDirectory.objects_by_uuid:
            obj = ServerDirectory.objects_by_uuid[uuid]
            state["objects"].append({
                "type": type(obj).__name__,
                "value": {
                    "uuid": uuid,
                    "x": obj.x,
                    "y": obj.y,
                    "action": obj.sprite.action,
                    "direction": obj.sprite.direction,
                    "index": obj.sprite.index
                }
            })
        return state
