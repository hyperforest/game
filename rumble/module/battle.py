from .interface import clear, wait

class RumbleStatus:
    def __init__(self):
        self.is_alive = True

class Arena:
    def __init__(self, length=1000):
        self.length = length
        self.tiles = {i : [] for i in range(- length // 2, 1 + length // 2)}

    def move(self, player, destination):
        source = player.status.location
        index = self.tiles[source].index(player)
        self.tiles[source].pop(index)
        self.tiles[destination].append(player)

class Rumble:
    def __init__(self, game, num_players=10):
        self.game = game
        self.num_players = num_players
        self.humans = game.players
        self.bots = []
        self.all = self.humans + self.bots
        self.arena = Arena()

    def spawn(self):
        for _ in range(self.num_players):
            self.all[i].status = RumbleStatus()

        

    def _sort_by_atk_speed(self):
        def key(player):
            return player.role.atk_speed

        self.all = sorted(self.all, key=key, reverse=True)
