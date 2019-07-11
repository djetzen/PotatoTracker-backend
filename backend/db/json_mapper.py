from json import JSONEncoder

class JSONMapper(JSONEncoder):
    def default(self, o):
        return o.__dict__