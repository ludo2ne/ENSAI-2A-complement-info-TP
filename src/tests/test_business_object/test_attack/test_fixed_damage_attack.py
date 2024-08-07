from business_object.attack.fixed_damage_attack import FixedDamageAttack
from business_object.pokemon.attacker_pokemon import AttackerPokemon


class TestFixedDamageAttack:
    def test_compute_damage(self):
        # GIVEN
        power = 100
        basic_hit = FixedDamageAttack(power=power)

        pikachu = AttackerPokemon()
        venusaur = AttackerPokemon()

        # WHEN
        damage = basic_hit.compute_damage(pikachu, venusaur)

        # THEN
        assert power == damage
