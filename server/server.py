import sys
from os import listdir
from os.path import isfile
from os.path import join
from messengers.messenger_for_server import MessengerForServer
from services.source_code_manager import SourceCodeManager
from services.ai_manager import AIManager
from services.surface import Surface
from cache.world_cache import WorldCache
from time import sleep

print("Starting ZelPy server")

#ip = sys.argv[1]
#port = int(sys.argv[2])
ip = "0.0.0.0"
port = 5005
source_code = SourceCodeManager(
    [f for f in listdir("./") if isfile(join("./", f))])
ai = AIManager()
messenger = MessengerForServer(ip, port)
cache = WorldCache()
surface = Surface()

# cache.load()

while True:
    # cache.save()
    source_code.check_files()
    ai.make_moves()
    surface.update()
    messenger.update_all_players()
    sleep(0.01)
