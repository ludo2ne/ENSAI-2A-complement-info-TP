from dataclasses import dataclass

from business_object.pokemon.abstract_pokemon import AbstractPokemon


@dataclass
class Round:
    attacker: AbstractPokemon
    defender: AbstractPokemon
    dealt_damage: int
    attack_description: str

    def __str__(self):
        res = "Attacker : " + str(self.attacker.name)
        res += ", Defender : " + str(self.defender.name)
        res += " --- " + str(self.attack_description)
        res += ", damages : " + str(self.dealt_damage)
        return res
