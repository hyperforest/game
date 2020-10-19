import random
from pandas import DataFrame, option_context
from .arena import StandardArena
from .backend import Prompt
from .battle_utils import random_bots_from_humans, Human, Bot
from .interface import clear, wait, query, generate_text_box
from .interface import CHOOSE_ROLE, BATTLE
from .role import get_role

class _BattlePrompt(Prompt):
    def __init__(self, battle):
        super().__init__()
        self.battle = battle

    def build(self):
        self.options = [self.player_details, self.player_location, self.quit]

    def ask(self):
        return query(header=self.battle.generate_header() + BATTLE,
            num=len(self.options))

    def player_details(self):
        self.battle.player_details()

    def player_location(self):
        self.battle.arena.player_location()

    def quit(self):
        _ = query('Are you sure? (y/n)')
        if _.lower() == 'y':
            self.continue_ask = False

class Battle:
    def __init__(self, game, num_players, arena=None):
        self.game = game
        self.bots = []
        self.humans = []
        self.arena = arena or StandardArena(1000)
        
        self.turn = 0
        self.alive_players = []
        self.num_players = num_players
        self.num_alive_players = num_players
        self.num_defeated_players = 0
        self.num_alive_humans = game.num_players
        self.num_alive_bots = num_players - game.num_players

    def start(self):
        clear()
        self.prompt.run()

    def new(self):
        clear()
        print(CHOOSE_ROLE)

        self.humans = []
        for i in range(len(self.game.players)):
            index = query(f'Select Player {i + 1} role', return_int=True)
            player = get_role(index)(player=self.game.players[i])
            self.humans.append(Human(player))
        
        self.bots = random_bots_from_humans(self.humans, self.num_alive_bots)
        self.bots = [Bot(player) for player in self.bots]
        self.all_players = self.humans + self.bots
        self.alive_players = self.all_players[:]

        self.spawn()
        self.prompt = _BattlePrompt(self)
        self.arena.battle = self

    def spawn(self):
        random.shuffle(self.all_players)
        spawn_tiles = self.arena.get_spawn_tiles(num=self.num_players)
        for player, tile in zip(self.all_players, spawn_tiles):
            self.arena.tiles[tile].append(player)
            player.location = tile

    def increase_turn(self):
        self.turn += 1
        self.arena.increase_turn()

    def generate_header(self):
        message = ['Battle Summary']
        message += [f'Turn         : {self.turn}']
        message += [f'Alive        : {self.num_alive_players}']
        message += [f'Defeated     : {self.num_defeated_players}']
        message += [f'Alive Humans : {self.num_alive_humans}']
        message += [f'Alive Bots   : {self.num_alive_bots}']
        message = generate_text_box(message, align='left')
        return message

    def player_details(self):
        clear()

        columns = ['Name', 'Human/Bot', 'Alive', 'Level', 'HP', 'Atk. Speed']
        index = range(1, 1 + self.num_players)
        table = [{'Name': P.role.player.name,
            'Human/Bot': type(P).__name__,
            'Alive': P.is_alive, 
            'Level': P.role.player.level,
            'HP': P.role.hp,
            'Atk. Speed': P.role.atk_speed}
            for P in self.all_players]
        table = DataFrame(data=table)

        by = ['Human/Bot', 'Alive', 'HP', 'Atk. Speed', 'Level']
        ascending = False
        table = table.sort_values(by=by, ascending=ascending)
        table = table[columns]
        table.index = index
        
        print(generate_text_box('> Player Details <'))
        with option_context('display.max_rows', None,
            'display.max_columns', None):
            print(table)
        wait()

    def _sort_by_atk_speed(self):
        def key(player):
            return player.role.atk_speed
        self.alive_players = sorted(self.alive_players, key=key, reverse=True)


class Rumble10(Battle):
    def __init__(self, game):
        super().__init__(game=game,
            num_players=10,
            arena=StandardArena(length=1000))

class Rumble100(Battle):
    def __init__(self, game):
        super().__init__(game=game,
            num_players=100,
            arena=StandardArena(length=10000))
