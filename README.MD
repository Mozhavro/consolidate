# consolidate
Console based ASCII date sim


![icon](res/icon.png)

Made for [GameOff](https://itch.io/jam/game-off-2017) gamedev contest.

# deploy/build
1. Install requirements using pip. You probably want to use [virtualenv](https://virtualenv.pypa.io/en/stable/).

`pip install -r requirements.txt`

2. There is a build scripts to make an executable. `build.sh` for Unix based systems and `build.bat` for Windows. Windows executable requires `res` folder to be in the same directory. Linux build is fully standalone.


# todo

1. Refactoring!
2. Ability to set player name.
3. Ability to choose partner.
4. Pack resources apart from executable, so there is an ability to alter them (dialogs, scenes).
