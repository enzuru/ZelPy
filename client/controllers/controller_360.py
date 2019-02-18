from controllers.xbox360_controller import Controller


class Controller360:

    def __init__(self, ident):
        self.controller = Controller(ident)

    def get_buttons_pressed(self):
        buttons = []
        (
            self.PAD_UP,
            self.PAD_RIGHT,
            self.PAD_DOWN,
            self.PAD_LEFT
        ) = self.controller.get_pad()
        (
            self.BUTTON_A,
            self.B,
            self.X,
            self.Y,
            self.LEFT_BUMP,
            self.RIGHT_BUMP,
            self.BACK,
            self.START,
            self.DONT_WORK,
            self.LEFT_STICK_BTN,
            self.RIGHT_STICK_BTN
        ) = self.controller.get_buttons()
        if self.PAD_UP:
            buttons.append('up')
        if self.PAD_DOWN:
            buttons.append('down')
        if self.PAD_LEFT:
            buttons.append('left')
        if self.PAD_RIGHT:
            buttons.append('right')
        if self.BUTTON_A:
            buttons.append('a')
        return buttons
