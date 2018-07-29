import sys
import os
from os.path import getmtime


class AIManager:

    ai_by_id = {}

    @classmethod
    def make_moves(cls):
        for ai in cls.ai_by_id:
            ai.move()
