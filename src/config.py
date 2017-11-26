import json
import os


class Config:

    def __init__(self, path=None):
        base_dir = os.path.dirname(os.path.dirname(__file__))
        self.path = path or os.path.join(base_dir, "res/config.json")
        self._conf = self.load(self.path)

    def load(self, path):
        with open(path) as config_file:
            conf = json.load(config_file)
            return conf

    def __getattr__(self, instance, owner=None):
        return self.__dict__["_conf"][instance]

    # def __set__(self, instanse, value):
    #     self._conf[instanse] = value
