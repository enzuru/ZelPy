import bson


class BSONTranslator:

    def translate(self, data):
        letter = bson.loads(data)
        print(letter, flush=True)
        return letter
