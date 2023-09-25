from typing import List, Union

from utils.singleton import Singleton
from exception.attack_not_found_exception import AttackNotFoundException
from business_object.attack.abstract_attack import AbstractAttack
from client.attack_client import AttackClient


class AttackService(metaclass=Singleton):
    def get_attacks_from_webservice(
        self, limit: int = 100, offset: int = 0
    ) -> List[AbstractAttack]:
        attack_client = AttackClient()
        return attack_client.get_all_attack(limit=limit, offset=offset)

    def get_attack_with_identifier_from_webservice(
        self, identifier: Union[int, str]
    ) -> AbstractAttack:
        attack = AttackClient().get_attack(identifier)
        if attack is None:
            raise AttackNotFoundException(identifier)
        return attack
