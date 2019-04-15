import sys
import threading

from actors.game_loop import GameLoop

TICK_DELAY = 0.01

ip = sys.argv[1]
port = int(sys.argv[2])
loop = GameLoop.start(ip, port)


def tick() -> None:
    loop.ask({"msg": "wakeup"})
    timer = threading.Timer(TICK_DELAY, tick)
    timer.start()


print("Starting ZelPy server")
tick()
