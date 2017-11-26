from .window import Window
from .config import Config


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


        config = Config()
        game_model = GameModel(config)
        window = Window(game_model, screen)
        window.start()
        

class GameModel:
    def __init__(self, config):
        self._partner_name = config.partner_name
        self._statement = 1
