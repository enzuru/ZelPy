from handlers.handler import Handler
from services.player_directory import PlayerDirectory
from factories.player_factory import PlayerFactory


class RequestToJoinHandler(Handler):

    def execute(self):
        username = self.sender.username
        ip = self.sender.ip
        port = self.value['port']
        if PlayerDirectory.lookup(username) == None:
            player = PlayerFactory.create(username, ip, port)
            PlayerDirectory.add(player)
        else:
            player = PlayerDirectory.lookup(username)
            player.ip = ip
            player.port = port
            print(PlayerDirectory.lookup(username))
