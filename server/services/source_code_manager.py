import sys
import os
import threading
from os.path import getmtime

class SourceCodeManager:

    def __init__(self, files):
        self.files = files
        self.mtimes = [(f, getmtime(f)) for f in files]
        #self.thread = threading.Thread(target=self.check_files)
        #self.thread.start()

    def check_files(self):
        for f, mtime in self.mtimes:
            if getmtime(f) != mtime:
                os.execv(sys.executable, ['python3'] + sys.argv)
