from .window import Window
from .dialog import Dialog
from . import config
from . import resources


class Game:
    def start(self):
        game_model = GameModel(config)
        window = Window(game_model)
        window.start()
        

class GameModel:
    def __init__(self, config):
        self.partner_name = config.NAME.title()
        self._dialog = resources.load_dialog()

    def get_statement(self, id):
        return self._dialog[str(id)]

    def get_scene(self, title):
        return resources.get_scene(title)
