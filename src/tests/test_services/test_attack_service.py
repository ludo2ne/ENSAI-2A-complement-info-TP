import os
from unittest import TestCase, mock

from exception.attack_not_found_exception import AttackNotFoundException
from exception.pokemon_not_found_exception import PokemonNotFoundException
from services.attack_service import AttackService

"""
Comme l'url du web service est gérée par des variables d'environement, et que
nos tests sont unitaires et testent le moins de code possible il faut fixer
à la main l'url à contacter. Dans le cas présent c'est la même que celle
utilisé par l'application, mais dans la vraie vie on devrait utiliser un
web service de test dédié aux tests, voir mieux, "mocker" le web service
en entier, et ne pas vraiment le contacter pour éviter des problèmes de données
"""


@mock.patch.dict(os.environ, {"HOST_WEBSERVICE": "http://web-services.domensai.ecole"})
class TestAttackService(TestCase):
    def test_get_attack_id_1(self):
        # GIVEN
        identifier = 1
        attack_service = AttackService()

        # WHEN
        attack = attack_service.get_attack_with_identifier_from_webservice(identifier)

        # THEN
        self.assertEquals(identifier, attack.id)

    def test_get_pokemon_name_Pikachu(self):
        # GIVEN
        identifier = "Aeroblast"
        attack_service = AttackService()

        # WHEN
        attack = attack_service.get_attack_with_identifier_from_webservice(identifier)

        # THEN
        self.assertEquals(identifier, attack.name)

    def test_get_pokemon_name_not_found(self):
        # GIVEN
        identifier = "azerety"
        attack_service = AttackService()

        # WHEN
        with self.assertRaises(AttackNotFoundException):
            attack_service.get_attack_with_identifier_from_webservice(identifier)

        # THEN
