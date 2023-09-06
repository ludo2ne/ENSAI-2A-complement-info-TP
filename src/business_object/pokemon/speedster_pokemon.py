from business_object.attack.physical_attack import PhysicalFormulaAttack
from business_object.pokemon.abstract_pokemon import AbstractPokemon


class SpeedsterPokemon(AbstractPokemon):
    def __init__(
        self,
        id=None,
        stat_max=None,
        stat_current=None,
        level=None,
        name=None,
        gear=None,
        common_attacks=[],
    ) -> None:
        special_attack = PhysicalFormulaAttack(
            power=90,
            name="Shadow claw",
            description="{pokemon.name} hits with all the" "power of the darkness",
        )

        super().__init__(
            id=id,
            stat_max=stat_max,
            stat_current=stat_current,
            level=level,
            name=name,
            gear=gear,
            special_attack=special_attack,
            common_attacks=common_attacks,
        )

    def get_pokemon_attack_coef(self) -> float:
        return 1 + (self.speed_current + self.sp_atk_current) / 200
