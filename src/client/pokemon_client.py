import os
import requests

from client.attack_client import AttackClient
from business_object.pokemon.pokemon_factory import PokemonFactory
from business_object.pokemon.abstract_pokemon import AbstractPokemon


END_POINT = "/pokemon"


class PokemonClient:
    """Make call to the pokemon endpoint"""

    def __init__(self) -> None:
        self.__HOST = os.environ["HOST_WEBSERVICE"]

    def get_pokemon(self, pokemon_name: str) -> AbstractPokemon:
        req = requests.get(f"{self.__HOST}{END_POINT}/{pokemon_name}")

        # Chek if the request is ok
        pokemon = None
        if req.status_code == 200:
            raw_pkmn = req.json()

            # Get all attacks
            attacks = []
            attack_client = AttackClient()
            for raw_attack in raw_pkmn["attacks"]:
                attack = attack_client.get_attack(raw_attack["id"])
                if attack:
                    attacks.append(attack)

            pkmn_factory = PokemonFactory()
            pokemon = pkmn_factory.instantiate_pokemon(
                type=raw_pkmn["pokemon_type"],
                hp=raw_pkmn["statistic"]["hp"],
                attack=raw_pkmn["statistic"]["attack"],
                defense=raw_pkmn["statistic"]["defense"],
                sp_atk=raw_pkmn["statistic"]["spe_atk"],
                sp_def=raw_pkmn["statistic"]["spe_def"],
                speed=raw_pkmn["statistic"]["speed"],
                level=raw_pkmn["level"],
                name=raw_pkmn["name"],
                common_attacks=attacks,
            )
        return pokemon
