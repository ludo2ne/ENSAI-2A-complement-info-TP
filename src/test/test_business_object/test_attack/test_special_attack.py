import random
from unittest import TestCase

from business_object.attack.special_attack import SpecialFormulaAttack
from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.statistic import Statistic


class TestSpecialFormulaAttack(TestCase):
    def test_compute_damage(self):

        # GIVEN
        expected_damage = 65
        power = 100
        attack_spe = 100
        speed = 100
        defense_spe = 10
        special_hit = SpecialFormulaAttack(power=power)

        pikachu = AttackerPokemon(level=1,
                                  stat_current=Statistic(sp_atk=attack_spe,
                                                         speed=speed))
        venusaur = AttackerPokemon(stat_current=Statistic(sp_def=defense_spe))

        # Because the damage calculation involves some RNG we need to
        # specify a seed to always get the same result for the test
        random.seed(1)

        # WHEN
        damage = special_hit.compute_damage(pikachu, venusaur)

        # THEN
        self.assertEqual(expected_damage, damage)

    def test_get_defense_stat(self):

        # GIVEN
        sp_def = 10
        special_hit = SpecialFormulaAttack()
        venusaur = AttackerPokemon(stat_current=Statistic(sp_def=sp_def))

        # WHEN
        defense_stat = special_hit.get_defense_stat(defender=venusaur)

        # THEN
        self.assertEqual(sp_def, defense_stat)

    def test_get_attack_stat(self):

        # GIVEN
        sp_attack = 10
        special_hit = SpecialFormulaAttack()
        pikachu = AttackerPokemon(stat_current=Statistic(sp_atk=sp_attack))

        # WHEN
        attack_stat = special_hit.get_attack_stat(attacker=pikachu)

        # THEN
        self.assertEqual(sp_attack, attack_stat)
