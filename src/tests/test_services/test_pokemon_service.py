import os

from unittest import TestCase, TextTestRunner, TestLoader, mock

from client.pokemon_client import PokemonClient
from exception.pokemon_not_found_exception import PokemonNotFoundException
from services.pokemon_service import PokemonService

"""
Comme l'url du web service est gérée par des variables d'environement, et que
nos tests sont unitaires et testent le moins de code possible il faut fixer
à la main l'url à contacter. Dans le cas présent c'est la même que celle
utilisé par l'application, mais dans la vraie vie on devrait utiliser un
web service de test dédié aux tests, voir mieux, "mocker" le web service
en entier, et ne pas vraiment le contacter pour éviter des problèmes de données
"""


@mock.patch.dict(os.environ, {"HOST_WEBSERVICE": "http://web-services.domensai.ecole"})
class TestPokemonService(TestCase):
    def test_get_all_pokemon_ok(self):
        # GIVEN
        limit = 100
        pokemon_service = PokemonService()

        # WHEN
        pokemons = pokemon_service.get_pokemon_from_webservice(limit, 0)

        # THEN
        self.assertEqual(limit, len(pokemons))

    def test_get_pokemon_id_1(self):
        # GIVEN
        identifier = 1
        pokemon_service = PokemonService()

        # WHEN
        pokemon = pokemon_service.get_pokemon_with_identifier_from_webservice(
            identifier
        )

        # THEN
        self.assertEqual(identifier, pokemon.id)

    def test_get_pokemon_name_Pikachu(self):
        # GIVEN
        identifier = "Pikachu"
        pokemon_service = PokemonService()

        # WHEN
        pokemon = pokemon_service.get_pokemon_with_identifier_from_webservice(
            identifier
        )

        # THEN
        self.assertEqual(identifier, pokemon.name)

    def test_get_pokemon_name_not_found(self):
        # GIVEN
        identifier = "azerety"
        pokemon_service = PokemonService()

        # WHEN
        with self.assertRaises(PokemonNotFoundException):
            pokemon_service.get_pokemon_with_identifier_from_webservice(identifier)

        # THEN


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(
        TestLoader().loadTestsFromTestCase(TestPokemonService)
    )
