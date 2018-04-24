import socket
import threading
import bson
from gevent import monkey
from services.world import World
from services.player_directory import PlayerDirectory
from messages.state_of_world import StateOfWorld
from interpreters.interpreter_for_server import InterpreterForServer
from translators.bson_translator import BSONTranslator
from participants.player import Player

monkey.patch_all()
bson.patch_socket()

global PlayerDirectory


class MessengerForServer:

    def __init__(self, server_ip, server_port):
        self.translator = BSONTranslator()
        self.interpreter = InterpreterForServer()
        self.server_ip = server_ip
        self.server_port = server_port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind((self.server_ip, self.server_port))
        self.thread = threading.Thread(target=self.await_messages)
        self.thread.start()

    def await_messages(self):
        while True:
            data, ip = self.sock.recvfrom(1024)
            print(ip)
            translation = self.translator.translate(data)
            sender = PlayerDirectory.lookup_player(translation['sender'])
            if sender is None:
                sender = Player(translation['sender'], ip[0], None)
            messages = translation['messages']
            self.iterate_messages(sender, messages)

    def iterate_messages(self, sender, messages):
        for message in messages:
            request = self.interpreter.interpret(sender, message)
            if request is not None:
                request.execute()

    def update_all_players(self):
        message = StateOfWorld(World.get_state()).message()
        for username in PlayerDirectory.players_by_username:
            player = PlayerDirectory.players_by_username[username]
            self.send_message(player, message)

    def send_message(self, player, message):
        message = bson.dumps(message)
        try:
            return self.sock.sendto(message, (player.ip, player.port))
        except socket.error as serr:
            print("Can't send message: " + message)
            return None
