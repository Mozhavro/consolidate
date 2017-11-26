import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

NAME = "hanna"

SCENES_DIR = os.path.join(BASE_DIR, "res/scene/{name}".format(name=NAME))
DIALOG = os.path.join(BASE_DIR, "res/dialog/{name}.json".format(name=NAME))