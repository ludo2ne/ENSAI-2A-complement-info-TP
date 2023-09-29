from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session


class StartView(AbstractView):
    def __init__(self):
        self.__questions = [
            {
                "type": "list",
                "name": "choix",
                "message": f"Hello {Session().user_name}",
                "choices": [
                    "Connection",
                    "Battle",
                    "List pokemons",
                    "List attacks",
                    "Create a pokemon",
                    "Quit",
                ],
            }
        ]

    def display_info(self):
        with open("src/graphical_assets/banner.txt", "r", encoding="utf-8") as asset:
            print(asset.read())

    def make_choice(self):
        reponse = prompt(self.__questions)
        if reponse["choix"] == "Quit":
            pass

        elif reponse["choix"] == "Connection":
            from view.connection_view import ConnectionView

            return ConnectionView()

        elif reponse["choix"] == "Battle":
            from view.battle_view import BattleView

            return BattleView()

        elif reponse["choix"] == "List pokemons":
            from view.pokemon_list_view import PokemonListView

            return PokemonListView()

        elif reponse["choix"] == "List attacks":
            from view.attack_list_view import AttackListView

            return AttackListView()

        elif reponse["choix"] == "Create a pokemon":
            from view.create_pokemon_view import CreatePokemonView

            return CreatePokemonView()
