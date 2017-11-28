import os
import json

import config


def get_scene(title):
    resource_file_path = os.path.join(config.SCENES_DIR, "{title}.txt".format(title=title))
    with open(resource_file_path) as scene_file:
        return scene_file.read()


def load_dialog():
    with open(config.DIALOG) as dialog_file:
        return json.load(dialog_file)