from characters.link import Link


class Player:

    def __init__(self, username, ip, port, birthplace=(0, 0)):
        self.username = username
        self.ip = ip
        self.port = port
        x, y = birthplace
        self.character = Link(x, y)
