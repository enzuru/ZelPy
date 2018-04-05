class RequestToJoin:

    def __init__(self, username, port):
        self.username = username
        self.port = port

    def message(self):
        return {
            "sender": self.username,
            "messages": [{
                "type": "request_to_join",
                "value": {
                    "port": self.port
                }
            }]
        }
