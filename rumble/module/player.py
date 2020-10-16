from .interface import generate_text_box

class Player:
    def __init__(self, name, role, level=1):
        self.__level = level
        self.__exp = 0
        self.__role = role(level)
        self.__name = name

    def get_level(self):
        return self.__level

    def get_exp(self):
        return self.__exp

    def get_role(self):
        return self.__role

    def get_name(self):
        return self.__name

    def stats(self):
        message = 'Stats\n'
        message += f'Name    : {self.__name}\n'
        message += f'Role    : {self.__exp}\n'
        message += f'Level   : {self.__level}\n'
        message += f'Exp     : {self.__exp}'
        message = generate_text_box(message, align='left')
        print(message)

class Human(Player):
    def __init__(self, level, role, name):
        super().__init__(level, role, name)

class Bot(Player):
    def __init__(self, level, role, name):
        super().__init__(level, role, name)