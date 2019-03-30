import sys
import os
from os.path import getmtime


class AIDirectory:

    ai_by_uuid = {}

    @classmethod
    def make_moves(cls):
        for uuid in cls.ai_by_uuid:
            cls.ai_by_uuid[uuid].move()

    @classmethod
    def add(cls, ai):
        AIDirectory.ai_by_uuid[ai.uuid] = ai

    @classmethod
    def lookup(cls, uuid):
        if uuid in AIDirectory.ai_by_uuid:
            return AIDirectory.ai_by_uuid[uuid]
        else:
            return None

    @classmethod
    def remove(cls, uuid):
        AIDirectory.ai_by_uuid.pop(uuid, None)
