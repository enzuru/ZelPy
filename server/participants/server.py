from participants.participant import Participant

class Server(Participant):
    def __init__(self, ip: str) -> None:
        self.ip = ip
