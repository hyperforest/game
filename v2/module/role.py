from math import floor

def __get_stats_exponential(value, level, factor=0.1):
    result = value
    for _ in range(level - 1):
        result += floor(factor * result)
    return result

class Role(object):
    def __init__(self, 
            base_hp,
            base_atk,
            atk_speed,
            atk_range,
            move_speed,
            level=1):
        
        # base stats, private, can not be changed during survival
        self.__base_hp = __get_stats_exponential(base_hp, level)
        self.__base_atk = __get_stats_exponential(base_atk, level)
        self.__base_atk_speed = atk_speed
        self.__base_atk_range = atk_range
        self.__base_move_speed = move_speed
        self.level = level

        # stats, public, can be changed during survival
        self.hp = self.__base_hp
        self.atk = self.__base_atk
        self.atk_speed = self.__base_atk_speed
        self.atk_range = self.__base_atk_range
        self.move_speed = self.__base_move_speed

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

    def set_all_stats_to_level(self, level):
        self.hp = __get_stats_exponential(self.__base_hp, level)
        self.atk = __get_stats_exponential(self.__base_atk, level)

    def attack(self, other):
        remaining_hp = max(0, other.hp - self.atk)
        other.set_hp(remaining_hp)
        damage = self.atk
        return damage

class Knight(Role):
    def __init__(self, level=1):
        super(Knight, self).__init__(
            base_hp=100,
            base_atk=20,
            atk_speed=2,
            atk_range=2,
            move_speed=3,
            level=level)

class Archer(Role):
    def __init__(self, level=1):
        super(Archer, self).__init__(
            base_hp=100,
            base_atk=20,
            atk_speed=2,
            atk_range=10,
            move_speed=2,
            level=level)
