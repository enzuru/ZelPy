import random
import socket
from typing import List

import bson
import miniupnpc
from gevent import monkey

from interpreters.interpreter_for_client import InterpreterForClient
from messages.buttons_pressed import ButtonsPressed
from messages.message import Message
from messages.request_to_join import RequestToJoin
from participants.participant import Participant
from participants.server import Server
from translators.bson_translator import BSONTranslator

monkey.patch_all()
bson.patch_socket()


class MessengerForClient:
    def __init__(self, server_ip: str) -> None:
        self.translator = BSONTranslator()
        self.interpreter = InterpreterForClient()
        self.server_ip = server_ip
        self.server_port = 5005
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_sock.setblocking(False)
        self.connect_to_server()
        self.client_ip = "0.0.0.0"
        self.client_port = random.randint(5006, 6000)
        self.client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_sock.setblocking(False)
        self.client_sock.bind((self.client_ip, self.client_port))
        self.sender = Server(self.server_ip)
        self.setup_upnp()

    def setup_upnp(self) -> None:
        self.upnp = miniupnpc.UPnP()
        self.upnp.discoverdelay = 10
        self.upnp.discover()
        self.upnp.selectigd()
        self.upnp.addportmapping(
            self.client_port, "UDP", self.upnp.lanaddr, self.client_port, "ZelPy", ""
        )

    def connect_to_server(self) -> None:
        self.server_sock.connect((self.server_ip, self.server_port))

    def get_messages(self) -> None:
        try:
            data, ip = self.client_sock.recvfrom(1024)
            translation = self.translator.translate(data)
            messages = translation["messages"]
            self.iterate_messages(self.sender, messages)
        except:
            None

    def iterate_messages(self, sender: Participant, messages: List[Message]) -> None:
        for message in messages:
            request = self.interpreter.interpret(sender, message)
            if request is not None:
                request.execute()

    def request_to_join_game(self, username: str) -> None:
        message = RequestToJoin(username, self.client_port).message()
        self.send_message(message)

    def send_buttons_pressed(self, username: str, buttons: List[str]) -> None:
        message = ButtonsPressed(username, buttons).message()
        self.send_message(message)

    def send_message(self, message: Message) -> None:
        try:
            self.server_sock.sendobj(message)
        except socket.error as serr:
            print("Can't send message: " + str(message))
