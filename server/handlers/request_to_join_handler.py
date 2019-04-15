from directories.player_directory import PlayerDirectory
from factories.player_factory import PlayerFactory
from handlers.handler import Handler

class RequestToJoinHandler(Handler):
    def execute(self) -> None:
        username = self.sender.username
        ip = self.sender.ip
        port = self.value["port"]
        if PlayerDirectory.lookup(username) == None:
            player = PlayerFactory.create(username, ip, port)
        else:
            player = PlayerDirectory.lookup(username)
            player.ip = ip
            player.port = port
