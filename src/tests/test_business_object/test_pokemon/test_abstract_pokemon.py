from unittest.mock import patch

from business_object.pokemon.abstract_pokemon import AbstractPokemon
from business_object.statistic import Statistic


class TestAbstractPokemon:
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
        assert abstract_pokemon.level == 2

    @patch.multiple(AbstractPokemon, __abstractmethods__=set())
    def test_reset_actual_stat(self):
        # GIVEN
        abstract_pokemon = AbstractPokemon(
            stat_max=Statistic(
                hp=10, attack=11, defense=12, sp_atk=13, sp_def=14, speed=15
            ),
            stat_current=Statistic(
                hp=0, attack=0, defense=0, sp_atk=0, sp_def=0, speed=0
            ),
        )
        # WHEN
        abstract_pokemon.reset_actual_stat()

        # THEN
        assert 10 == abstract_pokemon.hp_current
        assert 11 == abstract_pokemon.attack_current
        assert 12 == abstract_pokemon.defense_current
        assert 13 == abstract_pokemon.sp_atk_current
        assert 14 == abstract_pokemon.sp_def_current
        assert 15 == abstract_pokemon.speed_current

    @patch.multiple(AbstractPokemon, __abstractmethods__=set())
    def test_get_hit_more_hp_than_damage(self):
        # GIVEN
        hit_point = 100
        damage = 50
        abstract_pokemon = AbstractPokemon(stat_current=Statistic(hp=hit_point))

        # WHEN
        abstract_pokemon.get_hit(damage)

        # THEN
        assert abstract_pokemon.hp_current == hit_point - damage

    @patch.multiple(AbstractPokemon, __abstractmethods__=set())
    def test_get_hit_more_damage_than_hp(self):
        # GIVEN
        damage = 100
        hit_point = 50
        abstract_pokemon = AbstractPokemon(stat_current=Statistic(hp=hit_point))

        # WHEN
        abstract_pokemon.get_hit(damage)

        # THEN
        assert abstract_pokemon.hp_current == 0
