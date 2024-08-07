from dao.type_attack_dao import TypeAttackDAO


class TestTypeAttackDao:
    def test_find_all_attack_type(self):
        # GIVEN
        type_attack_dao = TypeAttackDAO()

        # WHEN
        attack_types = type_attack_dao.find_all_attack_type()

        # THEN
        assert attack_types is not None

    def test_find_id_by_label_ok(self):
        # GIVEN
        type_attack_dao = TypeAttackDAO()
        label = "special attack"

        # WHEN
        id = type_attack_dao.find_id_by_label(label)

        # THEN
        assert id == 3

    def test_find_id_by_label_None_result(self):
        # GIVEN
        type_attack_dao = TypeAttackDAO()
        label = ""

        # WHEN
        id = type_attack_dao.find_id_by_label(label)

        # THEN
        assert id is None


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
