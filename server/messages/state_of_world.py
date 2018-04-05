class StateOfWorld:

    def __init__(self, state):
        self.state = state

    def message(self):
        return {
            "sender": "server",
            "messages": [{
                "type": "state_of_world",
                "value": self.state
            }]
        }
