import os

from client.attack_client import AttackClient
from unittest import TestCase, TextTestRunner, TestLoader, mock


"""
Comme l'url du web service est gérée par des variables d'environement, et que
nos tests sont unitaires et testent le moins de code possible il faut fixer
à la main l'url à contacter. Dans le cas présent c'est la même que celle
utilisé par l'application, mais dans la vraie vie on devrait utiliser un
web service de test dédié aux tests, voir mieux, "mocker" le web service
en entier, et ne pas vraiment le contacter pour éviter des problèmes de données
"""


@mock.patch.dict(os.environ, {"HOST_WEBSERVICE": "http://web-services.domensai.ecole"})
class TestAttackClient(TestCase):
    def test_get_attack_ok(self):
        # GIVEN
        attack_id = 1
        attack_client = AttackClient()

        # WHEN
        attack = attack_client.get_attack(attack_id)

        # THEN
        self.assertEqual(attack_id, attack.id)

    def test_get_attack_none(self):
        # GIVEN
        attack_id = 99999999
        attack_client = AttackClient()

        # WHEN
        attack = attack_client.get_attack(attack_id)

        # THEN
        self.assertIsNone(attack)

    def test_get_all_attack_ok(self):
        # GIVEN
        attack_client = AttackClient()

        # WHEN
        attacks = attack_client.get_all_attack()

        # THEN
        self.assertIsNotNone(attacks)


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(TestLoader().loadTestsFromTestCase(TestAttackClient))
