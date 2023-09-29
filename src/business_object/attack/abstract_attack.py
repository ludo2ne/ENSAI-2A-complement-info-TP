from abc import ABC, abstractmethod


class AbstractAttack(ABC):
    def __init__(
        self,
        id=None,
        power: int = None,
        name: str = None,
        description: str = None,
        accuracy: int = None,
        element: str = None,
    ):
        self._id = id
        self._power = power
        self._name = name
        self._description = description
        self.accuracy = accuracy
        self.element = element

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

    def __str__(self):
        res = "Attack : " + str(self._name)
        res += ", power : " + str(self._power)
        res += ", description : " + str(self._description)
        return res

    @property
    def power(self):
        return self._power

    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def type(self):
        return self._TYPE_NAME
