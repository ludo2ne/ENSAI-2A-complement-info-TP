from random import randint, random, choice
from typing import Tuple

from business_object.attack.abstract_attack import AbstractAttack
from business_object.battle.battle import Battle
from business_object.pokemon.abstract_pokemon import AbstractPokemon
from utils.singleton import Singleton


class BattleService(metaclass=Singleton):
    def resolve_battle(
        self, monstie_1: AbstractPokemon, monstie_2: AbstractPokemon
    ) -> Battle:
        """
        A battle is divide in round. Each round one pokemon will be
        the attacker, the other the defender.

        The battle ends when a pokémon has 0 hp or less.

        This method creates a Battle object, which contains all the
        damage inflicted and the state of the monsters each round.
        This object can be sent to a client to display the battle
        in a nice way.

        Args:
            monstie_1 (AbstractPokemon): a pokemon
            monstie_2 (AbstractPokemon): another pokemon

        Returns:
            Battle : all the battle sequence round by round

        """

        # Select the first attacker and defender
        attacker, defender = self.get_order(monstie_1, monstie_2)

        battle = Battle(first_monstie=attacker, second_monstie=defender)

        # The battle only ends when a Pokemon is down
        while attacker.hp_current > 0 and defender.hp_current > 0:
            attack_used = self.choose_attack(attacker)

            damage = attack_used.compute_damage(attacker=attacker, defender=defender)

            defender.get_hit(damage=damage)

            battle.add_round(
                attacker=attacker,
                defender=defender,
                dealt_damage=damage,
                attack_description=attack_used.description,
            )

            # switch the role
            attacker, defender = defender, attacker

        # Because of the switch the winner is the defenser now
        battle.winner = defender
        return battle

    def get_order(
        self, monstie_1: AbstractPokemon, monstie_2: AbstractPokemon
    ) -> Tuple[AbstractPokemon, AbstractPokemon]:
        """
        Determine the first pokemon to attack.
        It compute a random int in [0; 50[ and add it to the pokemon speed.
        The pokemon with the higher speed+rand strike first.
        Args:
            monstie_1 (AbstractPokemon):
            monstie_2 (AbstractPokemon):

        Returns:
            Tuple[AbstractPokemon, AbstractPokemon]: the order
        """

        speed_monstie1 = monstie_1.speed_current + randint(0, 50)
        speed_monstie2 = monstie_2.speed_current + randint(0, 50)

        # We do not want any draw. If there is on we reroll
        while speed_monstie1 == speed_monstie2:
            speed_monstie1 = monstie_1.speed_current + randint(0, 50)
            speed_monstie2 = monstie_2.speed_current + randint(0, 50)

        if speed_monstie1 > speed_monstie2:
            first, second = monstie_1, monstie_2
        elif speed_monstie1 < speed_monstie2:
            first, second = monstie_2, monstie_1

        return first, second

    def choose_attack(self, attacker: AbstractPokemon) -> AbstractAttack:
        """
        Choose the attack used by the pokemon randomly.
        Roll a float in [0;1] :
            <  0.75 : choose a  basic attack at random
            >= 0.75 : use the special attack

        Args:
            attacker (AbstractPokemon):

        Returns:
            AbstractAttack : an attack
        """

        roll = random()
        if roll < 0.75:
            selected_attack = choice(attacker.common_attacks)
        else:
            selected_attack = attacker.special_attack

        return selected_attack
