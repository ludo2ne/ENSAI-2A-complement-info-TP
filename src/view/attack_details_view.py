from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session

from services.attack_service import AttackService


class AttackDetailsView(AbstractView):
    def __init__(self, attack_name):
        self.__attack = AttackService().get_attack_with_identifier_from_webservice(
            attack_name
        )

        self.__questions = [
            {
                "type": "confirm",
                "message": "Wanna see another attack",
                "default": True,
            }
        ]

    def display_info(self):
        print(f"Hello {Session().user_name}, details of {self.__attack.name}")

    def make_choice(self):
        print(self.__attack)

        answers = prompt(self.__questions)

        if answers[0]:
            from view.attack_list_view import AttackListView

            return AttackListView()
        else:
            from view.start_view import StartView

            return StartView()
