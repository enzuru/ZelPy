import pprint
from typing import Any
from typing import Dict

import bson

class BSONTranslator:
    def __init__(self) -> None:
        self.pp = pprint.PrettyPrinter(indent=2)

    def translate(self, data: str) -> Dict[Any, Any]:
        letter: Dict[Any, Any]
        letter = bson.loads(data)
        self.pp.pprint(letter)
        return letter
