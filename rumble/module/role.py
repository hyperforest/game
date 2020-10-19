from math import floor
from .interface import generate_text_box

def get_role(index):
    return __role__[index - 1]

def _get_stats_exponential(base, level, factor=0.1):
    result = base
    for _ in range(level - 1):
        result += floor(factor * result)
    return result

def _get_stats_linear(base, level, diff=0):
    return base + (level - 1) * diff

class Player:
    def __init__(self, name, level=1):
        self.name = name
        self.level = level
        self.exp = 0

    def get_stats(self):
        stats = {
            'Name': self.name,
            'Level': self.level,
            'Exp': self.exp
        }
        return stats

    def stats(self):
        stats = self.get_stats()
        message = ['Stats']
        for k, v in stats.items():
            message.append(f'{k}\t: {v}')
        message = '\n'.join(message)
        message = generate_text_box(message, align='left')
        print(message)


class Role:
    def __init__(self, 
            player,
            base_hp,
            base_atk,
            atk_speed,
            atk_range,
            move_speed):

        self.player = player

        # base stats, private, can not be changed during battle
        self.__base_hp = _get_stats_exponential(base_hp, player.level)
        self.__base_atk = _get_stats_exponential(base_atk, player.level)
        self.__base_atk_speed = _get_stats_linear(atk_speed, player.level, 
            diff=1)
        self.__base_atk_range = _get_stats_linear(atk_range, player.level,
            diff=1)
        self.__base_move_speed = _get_stats_linear(move_speed, player.level,
            diff=10)

        # stats, public, can be changed during battle
        self.hp = self.__base_hp
        self.atk = self.__base_atk
        self.atk_speed = self.__base_atk_speed
        self.atk_range = self.__base_atk_range
        self.move_speed = self.__base_move_speed

    def get_stats(self):
        stats = {
            'HP': self.hp,
            'Atk': self.atk,
            'Atk. Speed': self.atk_speed,
            'Atk. Range': self.atk_range,
            'Move. Speed': self.move_speed
        }
        return stats

    def set_hp(self, value):
        if isinstance(value, int):
            self.hp = value
        elif isinstance(value, float):
            self.hp = floor(value * self.__base_hp)

    def set_atk(self, value):
        if isinstance(value, int):
            self.atk = value
        elif isinstance(value, float):
            self.atk = floor(value * self.__base_atk)

    def set_atk_speed(self, value):
        if isinstance(value, int):
            self.atk_speed = value
        elif isinstance(value, float):
            self.atk_speed = value * self.__base_atk_speed

    def set_atk_range(self, value):
        if isinstance(value, int):
            self.atk_range = value
        elif isinstance(value, float):
            self.atk_range = value * self.__base_atk_range

    def set_move_speed(self, value):
        if isinstance(value, int):
            self.move_speed = value
        elif isinstance(value, float):
            self.move_speed = value * self.__base_move_speed

    def attack(self, other):
        remaining_hp = max(0, other.hp - self.atk)
        other.set_hp(remaining_hp)
        damage = self.atk
        return damage

class Knight(Role):
    def __init__(self, player, level=1):
        super().__init__(
            player     = player,
            base_hp    = 100,
            base_atk   = 20,
            atk_speed  = 2,
            atk_range  = 2,
            move_speed = 3)

__role__ = [Knight]