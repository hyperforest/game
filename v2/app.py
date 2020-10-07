from module.game import Game
from module.interface import clear, query, wait, wrap, Prompt

HOME = '''
----------------------------------------
|              Survival                |
----------------------------------------

(1) New game
(2) Exit'''

@Prompt
class MainMenu:
    def ask():
        return query(HOME, num=3)

    def start():
        game = Game()
        game.start()

    def end():
        wrap('Thanks for Playing!', newline=True)
        wait()
        clear()
        # exit()

    functions = [start, end]
    stop = [end]

def main():
    menu = MainMenu()
    menu.run()

if __name__ == '__main__':
    main()


'''
@P
class Q:
  @prompt_function
  def a(self):
    print('a')
  @prompt_function
  def b(self):
    print('b')
'''