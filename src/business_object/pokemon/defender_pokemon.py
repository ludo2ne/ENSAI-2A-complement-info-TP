from src.business_object.pokemon.abstract_pokemon import AbstractPokemon


class DefenderPokemon(AbstractPokemon):

    def get_pokemon_attack_coef(self):
        """
        Compute a damage multiplier.

        Returns :
            float : the multiplier
        """
        return 1 + (self.attack_current + self.defense_current) / 200
