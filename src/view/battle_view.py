from InquirerPy import prompt
from InquirerPy.separator import Separator

from view.abstract_view import AbstractView
from view.session import Session

from services.pokemon_service import PokemonService
from services.battle_service import BattleService


class BattleView(AbstractView):
    def __init__(self):
        pokemon_list = [
            Separator("🔥Fire Starter"),
            "Charmander",
            Separator("🚿Water starter"),
            "Squirtle",
            Separator("🌱Grass starter"),
            "Bulbasaur",
        ]

        self.__questions = [
            {
                "type": "list",
                "message": "Select Pokemon 1",
                "choices": pokemon_list,
            },
            {
                "type": "list",
                "message": "Select Pokemon 2",
                "choices": pokemon_list,
            },
        ]

    def display_info(self):
        print(f"Hello {Session().user_name}, please choose some pokemons for a battle")

    def make_choice(self):
        answers = prompt(self.__questions)

        pokemon_service = PokemonService()

        pokemon1 = pokemon_service.get_pokemon_with_identifier_from_webservice(
            answers[0]
        )
        pokemon2 = pokemon_service.get_pokemon_with_identifier_from_webservice(
            answers[1]
        )

        pokemon1.level = 5
        pokemon2.level = 5

        print("Before battle")
        print(pokemon1)
        print(pokemon2)
        print("-" * 50)

        battle = BattleService().resolve_battle(monstie_1=pokemon1, monstie_2=pokemon2)

        print(battle)
        print("-" * 50)

        print("After battle")
        print(pokemon1)
        print(pokemon2)

        another_battle = prompt(
            [
                {
                    "type": "confirm",
                    "name": "continue",
                    "message": "Another Battle ?",
                    "default": True,
                }
            ]
        )

        if another_battle["continue"]:
            return BattleView()

        else:
            from view.start_view import StartView

            return StartView()
