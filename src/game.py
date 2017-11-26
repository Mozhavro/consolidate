from .window import Window
from .dialog import Dialog
from . import config
from . import resources


class Game:
    def start(self):
        screen = """
          ___ .~- ` `' "' ` -~. ____
         :~+.-`  .-"-.  .-"~._  `-.+~:
         !  /  -`     `       `'--~:.l
          :'         .              '.
         /
        /-".        :  .            \`
         .`      /.-"\ : `-  ^       :`
         ^      "`    `.    \:'._  \ `!`
        :     :-===-.    .-===-.\  .!/'.
         '.; /     .             : :
        : `.l   .mPm.\    .mPm.  |/    l
       .     :                   :':   |
           \ '        d:         ' /   :
      :     '-:        "        :-;:   `
      .       .     ._..._.     :::`   _
     /        ::               ;::;.   !
    .      .  :;:.           .::::;:   '
    . :  : :  `:::'.       .'::::;::.   \
    '/.  .  .  `::l '-. .-' '|:::::::.   ;
    : |: :: ::__`.-.        _.-.::::::_  ;
    .~"` \ \ :`"/    `-..- `     \"`//    "~.
   /      \ \ .   ___ /\ ___      .//        \
  :        \ \.-`  _.~l)=~  `' -.:"
  `         '/  .    ":`-.       \            :
        """
        dialog ="Hello, world!"

        game_model = GameModel(config)
        window = Window(game_model, screen)
        window.start()
        

class GameModel:
    def __init__(self, config):
        self._partner_name = config.NAME
        self._dialog = resources.load_dialog()

    def get_statement(id):
        return self.dialog[id]

    def get_scene(title):
        return resources.get_scene(title)
