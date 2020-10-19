from . import battle
from .backend import Prompt
from .battle import Rumble10, Rumble100
from .role import Player
from .role import get_role
from .interface import clear, wait, generate_text_box
from .interface import query, numbered_query, simple_query
from .interface import HOME
import pickle

MENU = '''
(1) Rumble!
(2) Big Rumble!
(3) Player stats
(4) Save game
(5) Back to home
'''

def _load_from_path(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

def load():
    save_name = query(message='Insert file name')
    if not save_name.endswith('.pkl'):
        save_name += '.pkl'
    result = _load_from_path(save_name)

    print('\nGame successfully loaded!')
    print('Press enter to start playing %s' % save_name)
    wait()
    return result

class _GamePrompt(Prompt):
    def __init__(self, game):
        super().__init__()
        self.game = game

    def build(self):
        self.options = [self.rumble10, self.rumble100, self.stats, self.save,
            self.back]

    def ask(self):
        return query(header=self.game.header + MENU,
            num=len(self.options))

    def stats(self):
        self.game.stats()

    def rumble10(self):
        battle = Rumble10(self.game)
        battle.new()
        battle.start()

    def rumble100(self):
        battle = Rumble100(self.game)
        battle.new()
        battle.start()

    def save(self):
        self.game.save()

    def back(self):
        self.continue_ask = False

class Game(object):
    def __init__(self):
        self.name = None
        self.players = []
        self.num_players = 0
        self.prompt = None
        self.header = ''

    def start(self):
        clear()
        self.prompt.run()

    def stats(self):
        for player in self.players:
            player.stats()
        wait()

    def new(self):
        clear()
        new_box = generate_text_box('New Game', h_margin=15)
        print(new_box)

        self.name = query(message='Insert game name        ')
        self.num_players = query(return_int=True,
            message='Enter number of players ')

        for i in range(1, 1 + self.num_players):
            name_message = ('Insert Player %d name    ' % i)
            name = simple_query(name_message)
            player = Player(name=name)
            self.players.append(player)

        self._create_header()
        self.prompt = _GamePrompt(self)

    def save(self):
        save_name = query(message='Insert file name')
        save_name += '.pkl'
        with open(save_name, 'wb') as f:
            pickle.dump(self, f)
        
        print('\nGame successfully saved!')
        print('Saved to %s' % save_name)
        wait()

    def _create_header(self):
        header = 'Game name: %s\n' % self.name
        header += 'Players:\n'

        for i in range(self.num_players):
            header += ('(%d) %s' % (i + 1,
                self.players[i].name))
            if i < self.num_players - 1:
                header += '\n'

        self.header = generate_text_box(header, align='left')

'''
1
CHON
4
Mario
Erick
Esiah
Nathan
1
1
1
1
1

'''