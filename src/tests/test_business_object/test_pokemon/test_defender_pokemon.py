from src.business_object.pokemon.defender_pokemon import DefenderPokemon
from src.business_object.statistic import Statistic


class TestDefenderPokemon:
    def test_get_coef_damage_type(self):
        # GIVEN
        snorlax = DefenderPokemon(stat_current=Statistic(attack=100, defense=100))

        # WHEN
        multiplier = snorlax.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 2


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
