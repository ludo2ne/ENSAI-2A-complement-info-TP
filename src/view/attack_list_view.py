from InquirerPy import prompt

from view.abstract_view import AbstractView
from view.session import Session

from services.attack_service import AttackService


class AttackListView(AbstractView):
    def __init__(self):
        list_attack_names = [
            p.name for p in AttackService().get_attacks_from_webservice(50)
        ]
        list_attack_names.append("retour")

        self.__questions = [
            {
                "type": "list",
                "message": "Select an Attack",
                "choices": list_attack_names,
            }
        ]

    def display_info(self):
        print(f"Hello {Session().user_name}, please choose an attack")

    def make_choice(self):
        answers = prompt(self.__questions)

        if answers[0] == "retour":
            from view.start_view import StartView

            return StartView()
        else:
            from view.attack_details_view import AttackDetailsView

            return AttackDetailsView(answers[0])
