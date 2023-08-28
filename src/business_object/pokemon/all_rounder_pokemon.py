from business_object.pokemon.abstract_pokemon import AbstractPokemon
from business_object.attack.special_attack import SpecialFormulaAttack


class AllRounderPokemon(AbstractPokemon):
    def __init__(
        self, stat_max=None, stat_current=None, level=0, name=None, common_attacks=[]
    ) -> None:
        special_attack = SpecialFormulaAttack(
            power=80,
            name="Dragon laser",
            description="{pokemon} a dark laser shoots a dark laser.".format(
                pokemon=name
            ),
        )

        # Calling the parent class constructor
        super().__init__(
            stat_max=stat_max,
            stat_current=stat_current,
            level=level,
            name=name,
            common_attacks=common_attacks,
            special_attack=special_attack,
        )

    def get_pokemon_attack_coef(self) -> float:
        return 1 + (self.sp_atk_current + self.sp_def_current) / 200
