from . import battle
from .backend import Prompt
from .role import Knight, Archer
from .interface import clear, wait, generate_text_box
from .interface import query, numbered_query, simple_query
from .interface import HOME, CHOOSE_ROLE
from .player import Human
from .role import get_role
import pickle

MENU = '''
(1) Rumble!
(2) Player stats
(3) Save game
(4) Back to home
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
        self.options = [self.battle, self.stats, self.save, self.back]
        self.stops = [self.back]

    def ask(self):
        return query(header=self.game.header + MENU,
            num=len(self.options))

    def stats(self):
        self.game.stats()

    def battle(self):
        # TO DO: should be start battle
        clear()
        print('under construction')

    def save(self):
        self.game.save()

    def back(self):
        clear()
    

class Game(object):
    def __init__(self):
        self.name = None
        self.players = []
        self.num_players = 1
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

        self.name = query(message='Insert game name')
        self.num_players = query(return_int=True,
            message='Enter number of players')

        for i in range(1, 1 + self.num_players):
            clear()
            
            SETUP = generate_text_box(
                ('Setup for player %d\n' % i) +
                ('(total: %d)' % self.num_players)
                )
            print(SETUP + CHOOSE_ROLE)
            role_message = ('Select player %d role' % i)
            name_message = ('Insert player %d name' % i)
            
            role_index = numbered_query(
                message=role_message,
                num=2, return_int=True)
            name = simple_query(name_message)

            role = get_role(role_index)
            player = Human(name=name, role=role)
            self.players.append(player)

        self._create_header()
        self.prompt = _GamePrompt(self)
        self.start()

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
                self.players[i].get_name()))
            if i < self.num_players - 1:
                header += '\n'

        self.header = generate_text_box(header, align='left')

'''
1
CHON
4
1
Mario Camarena
2
Erick Hansel
1
Esiah Camarena
2
Nathan Camarena
'''