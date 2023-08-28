class Statistic:
    """
    Inventory all the game statistics
    """

    def __init__(
        self,
        hp: int = 0,
        attack: int = 0,
        defense: int = 0,
        sp_atk: int = 0,
        sp_def: int = 0,
        speed: int = 0,
    ):
        self.__hp = hp
        self.__attack = attack
        self.__defense = defense
        self.__sp_atk = sp_atk
        self.__sp_def = sp_def
        self.__speed = speed

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = value

    @property
    def attack(self):
        return self.__attack

    @attack.setter
    def attack(self, value):
        self.__attack = value

    @property
    def defense(self):
        return self.__defense

    @defense.setter
    def level(self, value):
        self.__defense = value

    @property
    def sp_atk(self):
        return self.__sp_atk

    @sp_atk.setter
    def sp_atk(self, value):
        self.__sp_atk = value

    @property
    def sp_def(self):
        return self.__sp_def

    @sp_def.setter
    def sp_def(self, value):
        self.__sp_def = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        self.__speed = value
