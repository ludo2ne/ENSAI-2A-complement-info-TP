from business_object.pokemon.abstract_pokemon import AbstractPokemon
from dao.pokemon_dao import PokemonDao


class TestPokemonDao:
    def test_find_all_pokemon(self):
        # GIVEN
        pokemon_dao = PokemonDao()

        # WHEN
        pokemons = pokemon_dao.find_all()

        # THEN

        assert len(pokemons) == 100
        assert isinstance(pokemons[1], AbstractPokemon)

    def test_find_pokemon_by_name(self):
        # GIVEN
        pokemon_dao = PokemonDao()
        pokemon_name = "Pikachu"

        # WHEN
        pokemon = pokemon_dao.find_pokemon_by_name(pokemon_name)

        # THEN
        assert pokemon_name == pokemon.name
        assert pokemon.common_attacks is not None


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
