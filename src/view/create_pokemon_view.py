from InquirerPy import prompt
from InquirerPy.validator import EmptyInputValidator

from view.abstract_view import AbstractView
from view.session import Session

from services.attack_service import AttackService
from business_object.pokemon.pokemon_factory import PokemonFactory


class CreatePokemonView(AbstractView):
    def __init__(self):
        list_types = ["Supporter", "Attacker", "Defender", "Speedster", "All-Rounder"]

        list_attack_names = [
            a.name for a in AttackService().get_attacks_from_webservice(20)
        ]

        self.__questions = [
            {
                "type": "input",
                "message": "Pokemon name : ",
                "validate": EmptyInputValidator(),
            },
            {
                "type": "list",
                "message": "Pokemon type : ",
                "choices": list_types,
            },
            {
                "type": "number",
                "message": "Pokemon level : ",
                "min_allowed": 1,
                "max_allowed": 100,
                "validate": EmptyInputValidator(),
            },
            {
                "type": "checkbox",
                "message": "Select some attacks (SPACE to select, ENTER to validate) : ",
                "choices": list_attack_names,
                "validate": lambda result: len(result) >= 1,
                "invalid_message": "should be at least 1 selection",
                "instruction": "(select at least 1)",
            },
        ]

    def display_info(self):
        print(f"Hello {Session().user_name}, please choose a pokemon")

    def make_choice(self):
        answers = prompt(self.__questions)

        # Get attacks from attack names
        attacks = []
        for attack_name in answers[3]:
            attacks.append(
                AttackService().get_attack_with_identifier_from_webservice(attack_name)
            )

        pokemon = PokemonFactory().instantiate_pokemon(
            name=answers[0],
            type=answers[1],
            level=answers[2],
            common_attacks=attacks,
        )

        if pokemon:
            print("successful creation")
            print(pokemon)
            Session().pokemon = pokemon

        from view.start_view import StartView

        return StartView()
