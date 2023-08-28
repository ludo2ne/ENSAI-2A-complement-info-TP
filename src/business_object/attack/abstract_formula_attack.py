from abc import abstractmethod
from random import uniform

from business_object.attack.abstract_attack import AbstractAttack
from business_object.pokemon.abstract_pokemon import AbstractPokemon


class AbstractFormulaAttack(AbstractAttack):
    def compute_damage(
        self, attacker: AbstractPokemon, defender: AbstractPokemon
    ) -> int:
        """
        Return the damage of the attack.

        The basic formula is : (yes it's the Pokemon damage formula)
            (((Niv×0.4+2)×Att×Pui)/(Def×50)+2)×pkemn_coefxother_modifier*random
        and we take the integer part.
        With
            Att = attacker's Attack or Special
            Def = defender's Defense or Special
            Pui = attack's power
            pkemn : attacker's damage multiplier
            other_modifier = all other modifiers (crit, status, etc)
            random = a random number between 0.85 an d1

        This method is not abstract anymore ! What does this mean ?
            - all sub attack will use the same formula
            - but it can be overridden
            - the Att and Def used for the calculation are not fixed

        To achieve this we need some other abstract methods :
            - get_attack_stat() : get the attacker stat_max (attack or spe_atk)
            - get_defense_stat() : get the defender stat_max (defense or spe_def)

        The the template method pattern for more info  :
            -> https://refactoring.guru/design-patterns/template-method

        Returns:
            int : the damage

        """
        raw_power = (
            (attacker.level * 0.4 + 2) * self.get_attack_stat(attacker) * self._power
        )

        raw_damage = raw_power / (self.get_defense_stat(defender) * 50) + 2

        rand = uniform(0.85, 1)

        final_damage = (
            raw_damage
            * attacker.get_pokemon_attack_coef()
            * self.other_modifier_atk(attacker)
            * self.other_modifier_def(defender)
            * rand
        )

        return int(final_damage)

    @abstractmethod
    def get_attack_stat(self, attacker: AbstractPokemon) -> float:
        """
        Get the stat_max use to compute the raw power of the attack.
        We keep the defender because we can want attack based on the
        defender stat like remaining hp.
        Args:
            attacker (AbstractPokemon): the attacker
        Returns:
            float : the used stat_max

        """
        pass

    @abstractmethod
    def get_defense_stat(self, defender: AbstractPokemon) -> float:
        """
        Get the stat_max use to compute the raw damage of the attack.
        We keep the attacker because we can want damage reduction based
        on the attacker stat like max hp.
        Args:
            defender (AbstractPokemon): the defender

        Returns:
            float : the used stat_max

        """
        pass

    def other_modifier_atk(self, attacker: AbstractPokemon) -> float:
        """
        Compute all the other modifiers (status mod, etc)
        For this lab it's only a dummy function. It can be
        overridden if needed
        Args:
            attacker (AbstractPokemon): the attacker

        Returns:

        """
        return 1

    def other_modifier_def(self, defender: AbstractPokemon) -> float:
        """
        Compute all the other modifiers (status mod, etc)
        For this lab it's only a dummy function. It can be
        overridden if needed
        Args:
            defender (AbstractPokemon): the defender

        Returns:

        """
        return 1
