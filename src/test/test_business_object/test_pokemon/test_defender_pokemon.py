from unittest import TestCase, TextTestRunner, TestLoader

from business_object.pokemon.defender_pokemon import DefenderPokemon
from business_object.statistic import Statistic


class TestDefenderPokemon(TestCase):
    def test_get_coef_damage_type(self):
        # GIVEN
        snorlax = DefenderPokemon(
            stat_current=Statistic(attack=100, defense=100))

        # WHEN
        multiplier = snorlax.get_pokemon_attack_coef()

        # THEN
        self.assertEqual(32, multiplier)


if __name__ == '__main__':
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestDefenderPokemon))
