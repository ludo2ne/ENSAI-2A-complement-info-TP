from business_object.attack.abstract_formula_attack import AbstractFormulaAttack
from business_object.pokemon.abstract_pokemon import AbstractPokemon


class PhysicalFormulaAttack(AbstractFormulaAttack):
    _TYPE_NAME = "physical attack"

    def get_attack_stat(self, attacker: AbstractPokemon) -> float:
        return attacker.attack_current

    def get_defense_stat(self, defender: AbstractPokemon) -> float:
        return defender.defense_current
