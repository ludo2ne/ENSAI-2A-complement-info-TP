from unittest import TestCase, TextTestRunner, TestLoader

from dao.type_attack_dao import TypeAttackDAO


class TestTypeAttackDao(TestCase):
    def test_find_all_attack_type(self):
        # GIVEN
        type_attack_dao = TypeAttackDAO()
        # WHEN
        attack_types = type_attack_dao.find_all_attack_type()

        # THEN
        self.assertIsNotNone(attack_types)

    def test_find_id_by_label_ok(self):
        # GIVEN
        type_attack_dao = TypeAttackDAO()
        label = "special attack"
        # WHEN
        id = type_attack_dao.find_id_by_label(label)

        # THEN
        self.assertEqual(id, 3)

    def test_find_id_by_label_None_result(self):
        # GIVEN
        type_attack_dao = TypeAttackDAO()
        label = ""
        # WHEN
        id = type_attack_dao.find_id_by_label(label)

        # THEN
        self.assertIsNone(id)


if __name__ == "__main__":
    # Run the tests
    result = TextTestRunner(verbosity=2).run(
        TestLoader().loadTestsFromTestCase(TestTypeAttackDao)
    )
