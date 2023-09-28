from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session

from services.pokemon_service import PokemonService


class PokemonListView(AbstractView):
    def __init__(self):
        list_pokemon_name = [
            p.name for p in PokemonService().get_pokemon_from_webservice(30)
        ]
        list_pokemon_name.append("retour")

        self.__questions = [
            {
                "type": "list",
                "message": "Select Pokemon 1",
                "choices": list_pokemon_name,
            }
        ]

    def display_info(self):
        print(f"Hello {Session().user_name}, please choose a pokemon")

    def make_choice(self):
        answers = prompt(self.__questions)

        if answers[0] == "retour":
            from view.start_view import StartView

            return StartView()
        else:
            from view.pokemon_details_view import PokemonDetailsView

            return PokemonDetailsView(answers[0])
