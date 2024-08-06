from business_object.statistic import Statistic


class Pokemon:
    """
    A Pokemon
    """

    # -------------------------------------------------------------------------
    # Constructor
    # -------------------------------------------------------------------------

    def __init__(self, stat_current=None, level=0, name=None, type_pk=None):
        # -----------------------------
        # Attributes
        # -----------------------------
        self._stat_current: Statistic = stat_current
        self._level: int = level
        self._name: str = name
        self._type: str = type_pk

    # -------------------------------------------------------------------------
    # Methods
    # -------------------------------------------------------------------------

    def get_pokemon_attack_coef(self) -> float:
        """
        Compute a damage multiplier related to the pokemon type.

        Returns :
            float : the multiplier
        """
        if self._type == "Attacker":
            multiplier = 1 + (self.speed_current + self.attack_current) / 200
        elif self._type == "Defender":
            multiplier = 1 + (self.attack_current + self.defense_current) / 200
        elif self._type == "All rounder":
            multiplier = 1 + (self.sp_atk_current + self.sp_def_current) / 200
        elif self._type == "Speedster":
            multiplier = 1 + (self.speed_current + self.sp_atk_current) / 200
        elif self._type == "Supporter":
            multiplier = 1 + (self.sp_atk_current + self.defense_current) / 200
        else:
            raise Exception("type inconnu")

        return multiplier

    def level_up(self) -> None:
        """
        Increase the level by one
        """
        self._level += 1

    def get_hit(self, damage) -> None:
        """
        Decrease health point when receiving damages
        """
        if damage > 0:
            if damage < self.hp_current:
                self.hp_current -= damage
            else:
                self.hp_current = 0

    def __str__(self):
        res = "I am " + str(self.name)
        res += ", level : " + str(self.level)
        res += ", attack coef : " + str(self.get_pokemon_attack_coef())
        return res

    # -------------------------------------------------------------------------
    # Getters and Setters
    # -------------------------------------------------------------------------

    @property
    def attack_current(self):
        return self._stat_current.attack

    @attack_current.setter
    def attack_current(self, value):
        self._stat_current.attack = value

    @property
    def hp_current(self):
        return self._stat_current.hp

    @hp_current.setter
    def hp_current(self, value):
        self._stat_current.hp = value

    @property
    def defense_current(self):
        return self._stat_current.defense

    @defense_current.setter
    def defense_current(self, value):
        self._stat_current.defense = value

    @property
    def sp_atk_current(self):
        return self._stat_current.sp_atk

    @sp_atk_current.setter
    def sp_atk_current(self, value):
        self._stat_current.sp_atk = value

    @property
    def sp_def_current(self):
        return self._stat_current.sp_def

    @sp_def_current.setter
    def sp_def_current(self, value):
        self._stat_current.sp_def = value

    @property
    def speed_current(self):
        return self._stat_current.speed

    @speed_current.setter
    def speed_current(self, value):
        self._stat_current.speed = value

    # Basic Getter / Setter
    @property
    def stat(self):
        return self.stat

    @property
    def level(self):
        return self._level

    @property
    def name(self):
        return self._name
