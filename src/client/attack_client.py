import os
import requests

from typing import List, Optional
from business_object.attack.attack_factory import AttackFactory
from business_object.attack.abstract_attack import AbstractAttack
from utils.singleton import Singleton

END_POINT = "/attack"


class AttackClient(metaclass=Singleton):
    def __init__(self) -> None:
        # Utilisation d'une variable d'environnement définie dans le fichier .env
        self.__HOST = os.environ["HOST_WEBSERVICE"]

    def get_attack(self, id: int) -> Optional[AbstractAttack]:
        """
        Get a specific attack from the webservice by calling the GET endpoint
        with a specific resource identifier.Do not raise any
        exception if any attack is found, just return None.

        :param id: attack id wanted
        :type id: int
        :return: The attack object with all value if the attack is found.
                 else None
        :rtype: AbstractAttack
        """
        url = f"{self.__HOST}{END_POINT}/{id}"
        req = requests.get(url)

        attack = None

        # Check if the request is ok
        if req.status_code == 200:
            raw_attack = req.json()
            attack_factory = AttackFactory()
            attack = attack_factory.instantiate_attack(
                type=raw_attack["attack_type"],
                id=raw_attack["id"],
                power=raw_attack["power"],
                name=raw_attack["name"],
                description=raw_attack["description"],
            )

        return attack

    def get_all_attack(self, limit: int = 0, offset: int = 0) -> List[AbstractAttack]:
        """
        Get all attack of the webservice by calling the GET endpoint. If there
        is some umprocessable attack because of there type
        , these attacks are skiped.

        :param limit: how many attack are returned at max, defaults to 0.
        :type limit: int, optional
        :param offset: the offset parameters of the endpoint, defaults to 0
        :type offset: int, optional
        :return: The list of all instanciated attack.
        :rtype: List[AbstractAttack]
        """
        # Check if the limit and offset need to be used.
        params = {}
        if limit > 0:
            params["limit"] = limit
        if offset > 0:
            params["offset"] = offset

        req = requests.get(f"{self.__HOST}{END_POINT}", params=params)

        # Check if the request is ok
        attacks = []
        if req.status_code == 200:
            raw_attacks = req.json()["results"]
            attack_factory = AttackFactory()
            for raw_attack in raw_attacks:
                attack = attack_factory.instantiate_attack(
                    type=raw_attack["attack_type"],
                    id=raw_attack["id"],
                    name=raw_attack["name"],
                )
                if attack:
                    attacks.append(attack)
        return attacks

    def create_attack(self, attack: AbstractAttack) -> bool:
        """
        Call the POST endpoint to create an attack

        :param attack: an already instanciated attack.
        :type attack: AbstractAttack
        :return: True is the ressource was created (code 201). False otherwise.
        :rtype: bool
        """
        # The requests'body. It's the "json" representation of an attack
        # used by the web service
        payload = {
            "name": attack.name,
            "attack_type": attack.type,
            "power": attack.power,
            "description": attack.description,
            "accuracy": attack.accuracy,
            "element": attack.element,
        }
        req = requests.post(f"{self.__HOST}{END_POINT}", json=payload)

        created = False
        if req.status_code == 201:
            created = True
        return created

    def update_attack(self, attack: AbstractAttack) -> bool:
        """
        Call the PUT endpoint to update or create a attack resource

        :param attack: an already instanciated attack.
        :type attack: AbstractAttack
        :return: True is the request was a sucess, False otherwise
        :rtype: bool
        """

        # The requests'body. It's the "json" representation of an attack
        # used by the web service
        payload = {
            "name": attack.name,
            "attack_type": attack.type,
            "power": attack.power,
            "description": attack.description,
            "accuracy": attack.accuracy,
            "element": attack.element,
        }
        params = {"attack_name": attack.id}
        req = requests.put(
            f"{self.__HOST}{END_POINT}/{attack.id}", params=params, json=payload
        )

        updated = False
        if req.status_code == 200:
            updated = True
        return updated

    def delete_attack(self, attack: AbstractAttack) -> bool:
        """
        Delete an attack resource by calling the DELETE endpoint.

        :param attack: An already instantiate attack
        :type attack: AbstractAttack
        :return: True is the request was successful, False otherwise
        :rtype: bool
        """
        req = requests.delete(f"{self.__HOST}{END_POINT}/{attack.name}")

        deleted = False
        if req.status_code == 200:
            deleted = True
        return deleted


if __name__ == "__main__":
    # Pour charger les variables d'environnement contenues dans le fichier .env
    import dotenv

    dotenv.load_dotenv(override=True)

    attack_client = AttackClient()

    attack_id = 1
    attack_client.get_attack(attack_id)
