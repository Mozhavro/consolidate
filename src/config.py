import json


class Config:

    def __init__(self, path=None):
        if path:
            self.path = path
        else:
            self.path = "../res/config.json"

        self._conf = self.load(path)

    def load(path):
        with open(path) as config_file:
            conf = json.load(config_file)
            return conf

    def __get__(self, instance, owner):
        return self._conf.get(instance, None)