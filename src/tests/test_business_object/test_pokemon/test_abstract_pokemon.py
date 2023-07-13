from unittest import TestCase, TextTestRunner, TestLoader
from unittest.mock import patch

from business_object.pokemon.abstract_pokemon import AbstractPokemon
from business_object.statistic import Statistic


class TestAbstractPokemon(TestCase):

    # Ok that's a little tricky. Here I want to test a method
    # of an abstract class. But I cannot instantiate abstract class
    # with abstract method.
    # However, level_up is not an abstract method. Thus, I don't
    # need to define it in a sub class.
    # So I need to patch my code juste for the test, and say to python
    # AbstractPokemon does not have any abstract method, so I can
    # create an instance and test my methode which is not abstract.
    @patch.multiple(AbstractPokemon, __abstractmethods__=set())
    def test_level_up(self):
        # GIVEN
        abstract_pokemon = AbstractPokemon(level=1)
        # WHEN
        abstract_pokemon.level_up()
        # THEN
        self.assertEqual(2, abstract_pokemon.level)

    @patch.multiple(AbstractPokemon, __abstractmethods__=set())
    def test_reset_actual_stat(self):
        # GIVEN
        abstract_pokemon = AbstractPokemon(
            stat_max=Statistic(hp=10, attack=11, defense=12, sp_atk=13, sp_def=14, speed=15), stat_current=Statistic(hp=0, attack=0, defense=0, sp_atk=0, sp_def=0, speed=0))
        # WHEN
        abstract_pokemon.reset_actual_stat()
        # THEN
        self.assertEqual(10, abstract_pokemon.hp_current)
        self.assertEqual(11, abstract_pokemon.attack_current)
        self.assertEqual(12, abstract_pokemon.defense_current)
        self.assertEqual(13, abstract_pokemon.sp_atk_current)
        self.assertEqual(14, abstract_pokemon.sp_def_current)
        self.assertEqual(15, abstract_pokemon.speed_current)

    @patch.multiple(AbstractPokemon, __abstractmethods__=set())
    def test_get_hit_more_hp_than_damage(self):
        # GIVEN
        hit_point = 100
        damage = 50
        abstract_pokemon = AbstractPokemon(
            stat_current=Statistic(hp=hit_point))

        # WHEN
        abstract_pokemon.get_hit(damage)

        # THEN
        self.assertEqual(hit_point-damage, abstract_pokemon.hp_current)

    @patch.multiple(AbstractPokemon, __abstractmethods__=set())
    def test_get_hit_more_damage_than_hp(self):
        # GIVEN
        damage = 100
        hit_point = 50
        abstract_pokemon = AbstractPokemon(
            stat_current=Statistic(hp=hit_point))

        # WHEN
        abstract_pokemon.get_hit(damage)

        # THEN
        self.assertEqual(0, abstract_pokemon.hp_current)


if __name__ == '__main__':
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestAbstractPokemon))
