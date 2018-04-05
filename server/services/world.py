from services.player_directory import PlayerDirectory

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
            player =  PlayerDirectory.players_by_username[username]
            state["objects"].append({
                "type": "link",
                "value": {
                    "uuid": player.character.uuid,
                    "x": player.character.x,
                    "y": player.character.y
                }
            })
        return state
