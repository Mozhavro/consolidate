from .window import Window


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

        window = Window(screen)
        window.start()
        # window = Window(screen, dialog)
        # window.render()
        