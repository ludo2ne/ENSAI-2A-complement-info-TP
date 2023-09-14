import time
from unittest import TestCase, TextTestRunner, TestLoader
from business_object.attack.special_attack import SpecialFormulaAttack

from dao.attack_dao import AttackDao


class TestAttackDao(TestCase):
    def test_find_all_attacks(self):
        # GIVEN
        attack_dao = AttackDao()
        # WHEN
        attacks = attack_dao.find_all_attacks(100)

        # THEN
        self.assertEqual(100, len(attacks))

    def test_find_attack_by_id_ok(self):
        # GIVEN
        attack_dao = AttackDao()
        # WHEN
        attack = attack_dao.find_attack_by_id(1)

        # THEN
        self.assertEqual(1, attack.id)

    def test_find_attack_by_id_not_found(self):
        # GIVEN
        attack_dao = AttackDao()
        # WHEN
        attack = attack_dao.find_attack_by_id(-1)

        # THEN
        self.assertIsNone(attack)

    def test_create_attack_ok(self):
        # GIVEN
        attack_dao = AttackDao()
        attack = SpecialFormulaAttack(
            power=10,
            name=f"test{time.time()}",
            description="ceci est un test",
            accuracy=10,
            element="foudre",
        )
        # WHEN
        created = attack_dao.add_attack(attack)

        # THEN
        self.assertTrue(created)
        self.assertIsNotNone(attack.id)

    def test_update_attack_ok(self):
        # GIVEN
        attack_dao = AttackDao()
        attack = SpecialFormulaAttack(
            id=1,
            power=10,
            name=f"test{time.time()}",
            description="ceci est un test",
            accuracy=10,
            element="foudre",
        )
        # WHEN
        updated = attack_dao.update_attack(attack)

        # THEN
        self.assertTrue(updated)

    def test_update_attack_ko(self):
        # GIVEN
        attack_dao = AttackDao()
        attack = SpecialFormulaAttack(
            id=-1,
            power=10,
            name=f"test{time.time()}",
            description="ceci est un test",
            accuracy=10,
            element="foudre",
        )
        # WHEN
        updated = attack_dao.update_attack(attack)

        # THEN
        self.assertFalse(updated)


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner(verbosity=2).run(
        TestLoader().loadTestsFromTestCase(TestAttackDao)
    )
