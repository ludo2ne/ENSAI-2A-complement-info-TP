import time
from business_object.attack.special_attack import SpecialFormulaAttack

from dao.attack_dao import AttackDao


class TestAttackDao:
    def test_find_all_attacks(self):
        # GIVEN
        attack_dao = AttackDao()

        # WHEN
        attacks = attack_dao.find_all_attacks(100)

        # THEN
        assert len(attacks) == 100

    def test_find_attack_by_id_ok(self):
        # GIVEN
        attack_dao = AttackDao()

        # WHEN
        attack = attack_dao.find_attack_by_id(1)

        # THEN
        assert attack.id == 1

    def test_find_attack_by_id_not_found(self):
        # GIVEN
        attack_dao = AttackDao()

        # WHEN
        attack = attack_dao.find_attack_by_id(-1)

        # THEN
        assert attack is None

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
        assert created
        assert attack.id is not None

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
        assert updated

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
        assert not updated


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
