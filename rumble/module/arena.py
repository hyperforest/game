import random
from pandas import DataFrame, option_context
from .interface import clear, wait, query, generate_text_box

class BaseArena:
    def __init__(self, length=1000):
        self.battle = None
        self.length = length
        self.lmost = -length // 2
        self.rmost = length // 2
        self.tiles = {i:[] for i in range(self.lmost, self.rmost + 1)}

    def get_spawn_tiles(self, num=None, margin=1):
        num = num or self.length // 100
        result = random.sample(range(self.lmost, self.rmost + 1, 100), num)
        result = [random.choice([max(x - margin, self.lmost),
            min(x + margin, self.rmost)]) for x in result]
        return result

    def player_location(self):
        clear()

        columns = ['Name', 'Human/Bot', 'Alive', 'Location']
        index = range(1, 1 + self.battle.num_players)
        table = [{'Name': P.role.player.name,
            'Human/Bot': type(P).__name__,
            'Alive': P.is_alive, 
            'Location': P.location}
            for P in self.battle.all_players]
        table = DataFrame(data=table)

        by = ['Location']
        ascending = [True]
        table = table.sort_values(by=by, ascending=ascending)
        table = table[columns]
        table.index = index
        
        print(generate_text_box('> Player Details <'))
        with option_context('display.max_rows', None,
            'display.max_columns', None):
            print(table)
        wait()

    def move(self, player, destination):
        source = player.location
        index = self.tiles[source].index(player)
        self.tiles[source].pop(index)
        self.tiles[destination].append(player)

class StandardArena(BaseArena):
    def __init__(self, length=1000):
        super().__init__(length)
        self.turn_start_fog = 4
        self.start_fog = False
        self.fog = {i:False for i in range(self.lmost, self.rmost + 1)}
        self.last_fog = (self.lmost - 1, self.rmost + 1)

    def increase_turn(self):
        if self.battle.turn >= self.turn_start_fog:
            self.start_fog = True

        if self.start_fog:
            tile1, tile2 = self.last_fog
            self.fog[tile1] = True
            self.fog[tile2] = True
            self.last_fog = (tile1 + 1, tile2 - 1)

    def player_location(self):
        clear()

        columns = ['Name', 'Human/Bot', 'Alive', 'Location', 'Fog']
        index = range(1, 1 + self.battle.num_players)
        table = [{'Name': P.role.player.name,
            'Human/Bot': type(P).__name__,
            'Alive': P.is_alive, 
            'Location': P.location,
            'Fog': self.fog[P.location]}
            for P in self.battle.all_players]
        table = DataFrame(data=table)

        by = ['Location']
        ascending = [True]
        table = table.sort_values(by=by, ascending=ascending)
        table = table[columns]
        table.index = index
        
        print(generate_text_box('> Player Details <'))
        with option_context('display.max_rows', None,
            'display.max_columns', None):
            print(table)
        wait()