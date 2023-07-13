from dataclasses import dataclass

from business_object.pokemon.abstract_pokemon import AbstractPokemon


@dataclass
class Round:
    attacker: AbstractPokemon
    defender: AbstractPokemon
    dealt_damage: int
    attack_description: str
