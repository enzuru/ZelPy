from directories.player_directory import PlayerDirectory
from directories.server_directory import ServerDirectory


class World:

    def load():
        print("fuck")

    def save():
        print("fuck")

    def get_state():
        state = {
            "objects": []
        }
        for username in PlayerDirectory.players_by_username:
            player = PlayerDirectory.players_by_username[username]
            state["objects"].append({
                "type": "Link",
                "value": {
                    "uuid": player.character.uuid,
                    "x": player.character.x,
                    "y": player.character.y,
                    "action": player.character.sprite.action
                }
            })
        for uuid in ServerDirectory.objects_by_uuid:
            obj = ServerDirectory.objects_by_uuid[uuid]
            state["objects"].append({
                "type": type(obj).__name__,
                "value": {
                    "uuid": uuid,
                    "x": obj.x,
                    "y": obj.y,
                    "action": obj.sprite.action
                }
            })
        return state
