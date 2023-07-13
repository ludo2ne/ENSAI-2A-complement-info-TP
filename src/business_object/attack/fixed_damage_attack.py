from business_object.attack.abstract_attack import AbstractAttack
from business_object.pokemon.abstract_pokemon import AbstractPokemon


class FixedDamageAttack(AbstractAttack):

    def compute_damage(self,
                       attacker: AbstractPokemon,
                       defender: AbstractPokemon) -> int:
        return self.power
