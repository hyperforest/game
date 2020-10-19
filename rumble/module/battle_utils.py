import random
from itertools import product
from .role import get_role, Player

def random_bots_from_humans(humans, num_bots=1):
    # randomize level
    human_levels = [P.role.player.level for P in humans]
    min_level = max(min(human_levels) - 1, 1)
    max_level = max(human_levels) + 1
    levels = [random.randint(min_level, max_level) for _ in range(num_bots)]

    # randomize name
    with open('module/bot_name/colors.txt', 'r') as f:
        first = f.readlines()
        first = [s.strip() for s in first]
    with open('module/bot_name/animals.txt', 'r') as f:
        second = f.readlines()
        second = [s.strip() for s in second]
    names = random.sample(list(product(first, second)), num_bots)
    names = [f'{name[0]} {name[1]}' for name in names]
    
    # randomize role
    roles = [get_role(random.randint(1, 1)) for _ in range(num_bots)]
    
    # create the result
    result = []
    for role, name, level in zip(roles, names, levels):
        result.append(role(player=Player(name, level)))

    return result

class PlayerWrapper:
    def __init__(self, role):
        self.role = role
        self.is_alive = True
        self.location = 0

    def stats(self):
        player_stats = self.role.player.get_stats()
        _ = player_stats.pop('Exp')
        player_stats.update(self.role.get_stats())

        message = 'Stats\n'
        for k, v in player_stats.items():
            message += f'{k}\t: {v}'

        message = generate_text_box(message, align='left')
        print(message)

class Human(PlayerWrapper):
    def __init__(self, role):
        super().__init__(role)

class Bot(PlayerWrapper):
    def __init__(self, role):
        super().__init__(role)