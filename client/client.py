from os import listdir
from os.path import isfile, join
from services.window import Window
from messengers.messenger_for_client import MessengerForClient
from controllers.controller_360 import Controller360
from services.source_code_manager import SourceCodeManager
from services.game import Game
from time import sleep
import sys

username = sys.argv[1]
manager = SourceCodeManager(
    [f for f in listdir("./") if isfile(join("./", f))])
window = Window()
messenger = MessengerForClient()
controller = Controller360(int(sys.argv[2]))

print("Starting ZelPy client for " + username)

while window.done == False:
    manager.check_files()
    window.check_events()
    buttons = controller.get_buttons_pressed()
    if Game.joined == False:
        messenger.request_to_join_game(username)
    if len(buttons) > 0:
        messenger.send_buttons_pressed(username, buttons)
    sleep(0.001)
    window.update()

window.quit()
