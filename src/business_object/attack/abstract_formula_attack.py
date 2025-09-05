from abc import ABC, abstractmethod
from abstract_attack import AbstractAttack


class AbstractFormulaAttack(ABC, AbstractAttack):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_attack_stat(self) -> float:
        pass

    @abstractmethod
    def get_defense_stat(self) -> float:
        pass

    def compute_damage(self):
        return self.power
