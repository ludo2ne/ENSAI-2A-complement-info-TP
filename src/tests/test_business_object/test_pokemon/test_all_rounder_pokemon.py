from unittest import TestCase, TextTestRunner, TestLoader

from business_object.pokemon.all_rounder_pokemon import AllRounderPokemon
from business_object.statistic import Statistic


class TestAllRounderPokemon(TestCase):
    def test_get_coef_damage_type(self):
        # GIVEN
        spe_atk = 100
        spe_def = 100
        charizard = AllRounderPokemon(stat_current=Statistic(
            sp_atk=spe_atk,
            sp_def=spe_def
        ))

        # WHEN
        multiplier = charizard.get_pokemon_attack_coef()

        # THEN
        self.assertEqual(2, multiplier)


if __name__ == '__main__':
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestAllRounderPokemon))
