from business_object.attack.special_attack import SpecialFormulaAttack
from business_object.pokemon.abstract_pokemon import AbstractPokemon


class SupporterPokemon(AbstractPokemon):
    def __init__(
        self,
        id=None,
        stat_max=None,
        stat_current=None,
        level=None,
        name=None,
        common_attacks=[],
    ) -> None:
        special_attack = SpecialFormulaAttack(
            power=40,
            name="Healing Song",
            description="{pokemon.name} sings a beautiful song ",
        )

        super().__init__(
            id=id,
            stat_max=stat_max,
            stat_current=stat_current,
            level=level,
            name=name,
            special_attack=special_attack,
            common_attacks=common_attacks,
        )

    def get_pokemon_attack_coef(self) -> float:
        return 1 + (self.sp_atk_current + self.defense_current) / 200
