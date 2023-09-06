import os

from unittest import TestCase, TextTestRunner, TestLoader, mock
from client.pokemon_client import PokemonClient


"""
Comme l'url du web service est gérée par des variables d'environement, et que
nos tests sont unitaires et testent le moins de code possible il faut fixer
à la main l'url à contacter. Dans le cas présent c'est la même que celle
utilisé par l'application, mais dans la vraie vie on devrait utiliser un
web service de test dédié aux tests, voir mieux, "mocker" le web service
en entier, et ne pas vraiment le contacter pour éviter des problèmes de données
"""


@mock.patch.dict(os.environ, {"HOST_WEBSERVICE": "http://web-services.domensai.ecole"})
class TestPokemonClient(TestCase):
    def test_get_pikachu(self):
        # GIVEN
        pokemon_name = "Pikachu"
        pokemon_client = PokemonClient()

        # WHEN
        pokemon = pokemon_client.get_pokemon(pokemon_name)

        # THEN
        self.assertEqual(pokemon_name, pokemon.name)


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(TestLoader().loadTestsFromTestCase(TestPokemonClient))
