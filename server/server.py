from os import listdir
from os.path import getmtime, isfile, join
from messengers.messenger_for_server import MessengerForServer
from services.source_code_manager import SourceCodeManager
from cache.world_cache import WorldCache
from time import sleep

manager = SourceCodeManager([f for f in listdir("./") if isfile(join("./", f))])
messenger = MessengerForServer()
cache = WorldCache()

print("Starting ZelPy server")
#cache.load()

while True:
    #cache.save()
    manager.check_files()
    messenger.update_all_players()
    sleep(0.01)
