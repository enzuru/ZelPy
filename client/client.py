import sys
import threading

from actors.game_loop import GameLoop

TICK_DELAY = 0.01

username = sys.argv[1]
ip = sys.argv[2]
controller_id = sys.argv[3]
controller_type = sys.argv[4]
loop = GameLoop.start(username, ip, controller_id, controller_type)


def tick() -> None:
    loop.ask({"msg": "wakeup"})
    timer = threading.Timer(TICK_DELAY, tick)
    timer.start()


print("Starting ZelPy client for " + username)
tick()
