class Player:
    def __init__(self, name, role, level=1):
        self.__level = level
        self.__exp = 0
        self.__role = role(level)
        self.__name = name

    def get_name(self):
        return self.__name

    def get_chara_stats(self):
        pass

class Human(Player):
    def __init__(self, level, role, name):
        super().__init__(level, role, name)