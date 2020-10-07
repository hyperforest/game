from . import battle
from .role import Knight, Archer
from .interface import clear, query, simple_query, Prompt

PLAYER = None

MENU = '''
----------------------------------------
|              Main Menu               |
----------------------------------------

(1) Survival
(2) Back to home'''

CHOOSE_SURVIVOR = '''
----------------------------------------
|           Choose Your Role           |
----------------------------------------

(1) Knight
(2) Archer'''

@Prompt
class _GameStarter:
    def ask():
        return query(MENU, num=3)

    def battle():
        # should be start battle
        clear()
        print('under construction')

    def back():
        clear()

    functions = [battle, back]
    stop = [back]

class Game(object):
    def __init__(self):
        self.starter = _GameStarter()
        self.player = None

        clear()
        char = query(CHOOSE_SURVIVOR, num=2)
        name = simple_query('Insert your name')
        # TO DO: implement game start more

    def start(self):
        self.starter.run()
