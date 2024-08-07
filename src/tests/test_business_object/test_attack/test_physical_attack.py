import random

from business_object.attack.physical_attack import PhysicalFormulaAttack
from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.statistic import Statistic


class TestPhysicalFormulaAttack:
    def test_compute_damage(self):
        # GIVEN
        expected_damage = 87
        power = 100
        attack = 100
        speed = 100
        defense = 10
        basic_hit = PhysicalFormulaAttack(power=power)

        pikachu = AttackerPokemon(
            level=1, stat_current=Statistic(attack=attack, speed=speed)
        )
        venusaur = AttackerPokemon(stat_current=Statistic(defense=defense))

        # Because the damage calculation involves some RNG we need to
        # specify a seed to always get the same result for the test
        random.seed(1)

        # WHEN
        damage = basic_hit.compute_damage(pikachu, venusaur)

        # THEN
        assert damage == expected_damage

    def test_get_defense_stat(self):
        # GIVEN
        defense = 10
        basic_hit = PhysicalFormulaAttack()

        venusaur = AttackerPokemon(stat_current=Statistic(defense=defense))

        # WHEN
        defense_stat = basic_hit.get_defense_stat(defender=venusaur)

        # THEN
        assert defense == defense_stat

    def test_get_attack_stat(self):
        # GIVEN
        attack = 10
        basic_hit = PhysicalFormulaAttack()

        pikachu = AttackerPokemon(stat_current=Statistic(attack=attack))

        # WHEN
        attack_stat = basic_hit.get_attack_stat(attacker=pikachu)

        # THEN
        assert attack == attack_stat
