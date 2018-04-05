from controllers.xbox360_controller import Controller

class Controller360:

    def __init__(self, ident):
        self.controller = Controller(ident)

    def get_buttons_pressed(self):
        buttons = []
        (
            self.up,
            self.right,
            self.down,
            self.left
        ) = self.controller.get_pad()
        if self.up:
            buttons.append('up')
        if self.down:
            buttons.append('down')
        if self.left:
            buttons.append('left')
        if self.right:
            buttons.append('right')
        return buttons
