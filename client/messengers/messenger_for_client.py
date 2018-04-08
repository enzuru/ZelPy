import socket
import threading
import bson
import random
from gevent import monkey
from messages.request_to_join import RequestToJoin
from messages.buttons_pressed import ButtonsPressed
from interpreters.interpreter_for_client import InterpreterForClient
from participants.server import Server
from translators.bson_translator import BSONTranslator

monkey.patch_all()
bson.patch_socket()


class MessengerForClient:

    def __init__(self):
        self.translator = BSONTranslator()
        self.interpreter = InterpreterForClient()
        self.server_ip = "localhost"
        self.server_port = 5005
        self.server_sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )
        self.connect_to_server()
        self.client_ip = "127.0.0.1"
        self.client_port = random.randint(5006, 6000)
        self.client_sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_DGRAM
        )
        self.client_sock.bind((self.client_ip, self.client_port))
        self.thread = threading.Thread(target=self.await_messages)
        self.thread.start()

    def connect_to_server(self):
        self.server_sock.connect((self.server_ip, self.server_port))

    def await_messages(self):
        sender = Server(self.server_ip)
        while True:
            data, ip = self.client_sock.recvfrom(1024)
            translation = self.translator.translate(data)
            messages = translation["messages"]
            self.iterate_messages(sender, messages)

    def iterate_messages(self, sender, messages):
        for message in messages:
            request = self.interpreter.interpret(sender, message)
            if request is not None:
                request.execute()

    def request_to_join_game(self, username):
        message = RequestToJoin(username, self.client_port).message()
        self.send_message(message)

    def send_buttons_pressed(self, username, buttons):
        message = ButtonsPressed(username, buttons).message()
        self.send_message(message)

    def send_message(self, message):
        try:
            return self.server_sock.sendobj(message)
        except socket.error as serr:
            print("Can't send message: " + str(message))
            return None
