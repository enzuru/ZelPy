from handlers.request_to_join_handler import RequestToJoinHandler
from handlers.buttons_pressed_handler import ButtonsPressedHandler


class InterpreterForServer:

    message_types = {
        "request_to_join": RequestToJoinHandler,
        "buttons_pressed": ButtonsPressedHandler
    }

    def interpret(self, sender, message):
        if message['type'] in self.message_types:
            return self.message_types[message['type']](
                sender,
                message['value']
            )
        else:
            return None
