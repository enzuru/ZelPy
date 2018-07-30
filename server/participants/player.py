from characters.link import Link


class Player:

    def __init__(self, username, ip, port, create_character = False, birthplace=(0, 0)):
        self.username = username
        self.ip = ip
        self.port = port
        x, y = birthplace
        if create_character:
            self.character = Link(x, y)
