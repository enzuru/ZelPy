from handlers.state_of_world_handler import StateOfWorldHandler


class InterpreterForClient:

    message_types = {
        "state_of_world": StateOfWorldHandler
    }

    def interpret(self, sender, message):
        if message['type'] in self.message_types:
            return self.message_types[message['type']](
                sender,
                message['value']
            )
        else:
            return None
