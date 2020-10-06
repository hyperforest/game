from module.game import Game
from module.interface import clear, query, wait, wrap, Prompt

HOME = '''
----------------------------------------
|              Survival                |
----------------------------------------

(1) New game
(2) Exit'''

class MainMenu(Prompt):
    def get_opt(self):
        return query(HOME, num=3)

    def opt_1(self):
        game = Game()
        game.start()

    def opt_2(self):
        wrap('Thanks for Playing!', newline=True)
        wait()
        clear()
        return 0

def main():
    menu = MainMenu()
    get_opt = menu.get_opt
    functions = [menu.opt_1, menu.opt_2]
    menu.run(get_opt=get_opt, functions=functions)

if __name__ == '__main__':
    main()
