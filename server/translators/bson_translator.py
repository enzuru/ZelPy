import pprint
import bson


class BSONTranslator:

    def __init__(self):
        self.pp = pprint.PrettyPrinter(indent=2)

    def translate(self, data):
        letter = bson.loads(data)
        self.pp.pprint(letter)
        return letter
