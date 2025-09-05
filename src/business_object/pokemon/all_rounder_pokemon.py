from src.business_object.pokemon.abstract_pokemon import AbstractPokemon


class AllRounderPokemon(AbstractPokemon):

    def get_pokemon_attack_coef(self):
        """
        Compute a damage multiplier.

        Returns :
            float : the multiplier
        """
        return 1 + (self.sp_atk_current + self.sp_def_current) / 200
