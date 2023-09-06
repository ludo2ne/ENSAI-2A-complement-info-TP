import os
import time

from unittest import TestCase, TextTestRunner, TestLoader, mock
from client.attack_client import AttackClient
from business_object.attack.physical_attack import PhysicalFormulaAttack


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

    def test_create_attack_ok(self):
        # GIVEN
        attack_client = AttackClient()
        attack = PhysicalFormulaAttack(
            power=1000, name=f"test{time.time()}", description="a test"
        )

        # WHEN
        created = attack_client.create_attack(attack)

        # THEN
        self.assertTrue(created)

    def test_update_attack_ok(self):
        # GIVEN
        attack_client = AttackClient()
        attack = PhysicalFormulaAttack(
            id=50,
            power=1000,
            name=f"test{time.time()}",
            description="a test",
            accuracy=100,
            element="foudre",
        )

        # WHEN
        updated = attack_client.update_attack(attack)

        # THEN
        self.assertTrue(updated)

    def test_delete_attack_ok(self):
        # GIVEN
        attack_client = AttackClient()
        timestamp = time.time()
        attack = PhysicalFormulaAttack(
            power=1000, name=f"test{timestamp}", description="a test"
        )
        # Need an attack to run the delete. It's a pretty bad way to do
        # it but with the tools you know it's the best way :/
        attack_client.create_attack(attack)

        # WHEN
        deleted = attack_client.delete_attack(attack)

        # THEN
        self.assertTrue(deleted)


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner().run(TestLoader().loadTestsFromTestCase(TestAttackClient))
