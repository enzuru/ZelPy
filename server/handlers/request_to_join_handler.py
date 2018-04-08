from handlers.handler import Handler
from services.player_directory import PlayerDirectory
from factories.player_factory import PlayerFactory


class RequestToJoinHandler(Handler):

    def execute(self):
        username = self.sender.username
        ip = self.sender.ip
        port = self.value['port']
        if PlayerDirectory.lookup_player(username) == None:
            player = PlayerFactory.create(username, ip, port)
            PlayerDirectory.add_player(player)
        # print(PlayerDirectory.players_by_username)
