from business_object.pokemon.abstract_pokemon import AbstractPokemon
from business_object.attack.physical_attack import PhysicalFormulaAttack


class AttackerPokemon(AbstractPokemon):

    def __init__(self,
                 stat_max=None,
                 stat_current=None,
                 level=0,
                 name=None,
                 common_attacks=[]) -> None:

        special_attack = PhysicalFormulaAttack(
            power=60,
            name="Flying Strike",
            description="{pokemon} dives to it's prey from the sky")

        # Calling the parent class constructor
        super().__init__(stat_max=stat_max,
                         stat_current=stat_current,
                         level=level,
                         name=name,
                         common_attacks=common_attacks,
                         special_attack=special_attack)

    def get_pokemon_attack_coef(self) -> float:
        return 1 + (self.speed_current+self.attack_current)/200
