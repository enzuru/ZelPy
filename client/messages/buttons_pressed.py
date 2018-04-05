class ButtonsPressed:

    def __init__(self, username, buttons):
        self.username = username
        self.buttons = buttons

    def message(self):
        return {
            "sender": self.username,
            "messages": [{
                "type": "buttons_pressed",
                "value": {
                    "buttons": self.buttons
                }
            }]
        }
