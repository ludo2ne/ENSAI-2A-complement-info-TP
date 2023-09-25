from typing import List, Union

from utils.singleton import Singleton
from business_object.pokemon.abstract_pokemon import AbstractPokemon
from client.pokemon_client import PokemonClient
from exception.pokemon_not_found_exception import PokemonNotFoundException


class PokemonService(metaclass=Singleton):
    def get_pokemon_from_webservice(
        self, limit: int = 100, offset: int = 0
    ) -> List[AbstractPokemon]:
        """
        Request the webservice to get pokemons

        :param limit: How many pokemon are requested/returned
        :type limit: int
        :param offset: an offset for the request
        :type offset: int
        :return: Return a list of pokemons
        :rtype: List[AbstractPokemon]
        """

        return PokemonClient().get_all_pokemon(limit=limit, offset=offset)

    def get_pokemon_with_identifier_from_webservice(
        self, identifier: Union[int, str]
    ) -> AbstractPokemon:
        pokemon = PokemonClient().get_pokemon(identifier)
        if pokemon is None:
            raise PokemonNotFoundException(identifier)
        return pokemon
