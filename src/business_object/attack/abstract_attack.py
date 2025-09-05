from abc import ABC, abstractmethod


class AbstractAttack(ABC):
    """
    An Attack
    """

    def __init__(self, power=None, name=None, description=None):
        self._power: int = power
        self._name: str = name
        self._description: str = description

    @abstractmethod
    def compute_damage(self) -> int:
        pass
