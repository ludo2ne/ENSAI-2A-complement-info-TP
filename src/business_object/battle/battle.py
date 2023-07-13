from typing import List

from business_object.battle.round import Round
from business_object.pokemon.abstract_pokemon import AbstractPokemon


class Battle:
    def __init__(self,
                 first_monstie: AbstractPokemon,
                 second_monstie: AbstractPokemon) -> None:

        self.__first_monstie: AbstractPokemon = first_monstie
        self.__second_monstie: AbstractPokemon = second_monstie
        self.__rounds: List[Round] = []
        self.__winner: AbstractPokemon = None
        self.__final_phrase: str = ""

    def add_round(self,
                  attacker,
                  defender,
                  dealt_damage,
                  attack_description):
        self.__rounds.append(Round(attacker=attacker,
                                   defender=defender,
                                   dealt_damage=dealt_damage,
                                   attack_description=attack_description))

    @property
    def first_monstie(self):
        return self.__first_monstie

    @property
    def second_monstie(self):
        return self.__second_monstie

    @property
    def rounds(self):
        return self.__rounds

    @property
    def winner(self):
        return self.__winner

    @winner.setter
    def winner(self, value):
        self.__winner = value

    @property
    def final_phrase(self):
        return self.__final_phrase

    @final_phrase.setter
    def final_phrase(self, value):
        self.__final_phrase = value
