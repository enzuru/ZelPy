class PlayerDirectory:

    players_by_username = {}

    @classmethod
    def add_player(cls, player):
        PlayerDirectory.players_by_username[player.username] = player

    @classmethod
    def lookup_player(PlayerDirectory, username):
        if username in PlayerDirectory.players_by_username:
            return PlayerDirectory.players_by_username[username]
        else:
            return None

    @classmethod
    def get_players_by_username(cls):
        return PlayerDirectory.players_by_username
