import socket
from typing import List

import bson
from gevent import monkey

from directories.player_directory import PlayerDirectory
from interpreters.interpreter_for_server import InterpreterForServer
from messages.message import Message
from messages.state_of_world import StateOfWorld
from participants.participant import Participant
from participants.player import Player
from services.world import World
from translators.bson_translator import BSONTranslator

monkey.patch_all()
bson.patch_socket()


global PlayerDirectory
global ServerDirectory


class MessengerForServer:
    def __init__(self, server_ip: str, server_port: int) -> None:
        self.translator = BSONTranslator()
        self.interpreter = InterpreterForServer()
        self.server_ip = server_ip
        self.server_port = server_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setblocking(False)
        self.sock.bind((self.server_ip, self.server_port))
        self.last_state = None

    def get_messages(self) -> None:
        try:
            data, ip = self.sock.recvfrom(1024)
            translation = self.translator.translate(data)
            sender = PlayerDirectory.lookup(translation["sender"])
            if sender is None:
                sender = Player(translation["sender"], ip[0], None)
            messages = translation["messages"]
            self.iterate_messages(sender, messages)
        except:
            None

    def iterate_messages(self, sender: Participant, messages: List[Message]) -> None:
        for message in messages:
            request = self.interpreter.interpret(sender, message)
            if request is not None:
                request.execute()

    def update_all_players(self) -> None:
        message = StateOfWorld(World.get_state()).message()
        if message == self.last_state:
            return
        else:
            self.last_state = message
        for username in PlayerDirectory.players_by_username:
            player = PlayerDirectory.players_by_username[username]
            self.send_message(player, message)

    def send_message(self, player: Player, message: Message) -> None:
        message = bson.dumps(message)
        try:
            self.sock.sendto(message, (player.ip, player.port))
        except socket.error as serr:
            print("Can't send message: " + message)
            return None
