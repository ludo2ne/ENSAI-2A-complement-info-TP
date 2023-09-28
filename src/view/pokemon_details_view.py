from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session

from services.pokemon_service import PokemonService


class PokemonDetailsView(AbstractView):
    def __init__(self, pokemon_name):
        self.__pokemon = PokemonService().get_pokemon_with_identifier_from_webservice(
            pokemon_name
        )

        self.__questions = [
            {
                "type": "confirm",
                "message": "Wanna see another pokemon",
                "default": True,
            }
        ]

    def display_info(self):
        print(f"Hello {Session().user_name}, details of {self.__pokemon.name}")

    def make_choice(self):
        print(self.__pokemon)

        answers = prompt(self.__questions)

        if answers[0]:
            from view.pokemon_list_view import PokemonListView

            return PokemonListView()
        else:
            from view.start_view import StartView

            return StartView()
