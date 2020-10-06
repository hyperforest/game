from . import battle
from .role import Knight, Archer
from .interface import bar, clear, query, simple_query, wrap, Prompt

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

class GameStarter(Prompt):
    def get_opt(self):
        return query(MENU, num=3)

    def opt_1(self):
        # should be start battle
        clear()
        print('under construction')

    def opt_2(self):
        clear()
        return 0


class Game(object):
    def __init__(self):
        self.starter = GameStarter()
        self.player = None

        clear()
        char = query(CHOOSE_SURVIVOR, num=2)
        name = simple_query('Insert your name')
        # TO DO: implement game start more

    def start(self):
        get_opt = self.starter.get_opt
        functions = [self.starter.opt_1, self.starter.opt_2]
        self.starter.run(get_opt=get_opt, functions=functions)
