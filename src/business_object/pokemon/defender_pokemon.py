from business_object.pokemon.abstract_pokemon import AbstractPokemon
from business_object.attack.physical_attack import PhysicalFormulaAttack


class DefenderPokemon(AbstractPokemon):
    def __init__(
        self,
        id=None,
        stat_max=None,
        stat_current=None,
        level=0,
        name=None,
        common_attacks=[],
    ) -> None:
        special_attack = PhysicalFormulaAttack(
            power=60,
            name="Elbow tackle",
            description="{pokemon} hits with a massive tackle.".format(pokemon=name),
        )

        # Calling the parent class constructor
        super().__init__(
            id=id,
            stat_max=stat_max,
            stat_current=stat_current,
            level=level,
            name=name,
            common_attacks=common_attacks,
            special_attack=special_attack,
        )

    def get_pokemon_attack_coef(self) -> float:
        return 1 + (self.attack_current + self.defense_current) / 200
