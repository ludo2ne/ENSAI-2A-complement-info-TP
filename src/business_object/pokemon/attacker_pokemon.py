from src.business_object.pokemon.abstract_pokemon import AbstractPokemon


class AttackerPokemon(AbstractPokemon):

    def get_pokemon_attack_coef(self):
        """
        Compute a damage multiplier.

        Returns :
            float : the multiplier
        """
        return 1 + (self.speed_current + self.attack_current) / 200
