from abc import ABC, abstractmethod


class AbstractAttack(ABC):
    def __init__(self, power: int = None, name: str = None, description: str = None):
        self._power = power
        self._name = name
        self._description = description

    @abstractmethod
    def compute_damage(
        self, attacker: "AbstractPokemon", defender: "AbstractPokemon"
    ) -> int:
        """
         Return the damage of the attack.
         It's an abstract method because some attack will
         have variable damages, others have fixed damages

        Returns:
            int : the damage of the attack
        """
        pass

    @property
    def power(self):
        return self._power

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description
