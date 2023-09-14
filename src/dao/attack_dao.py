from typing import List, Optional
from utils.singleton import Singleton

from dao.db_connection import DBConnection
from dao.type_attack_dao import TypeAttackDAO

from business_object.attack.abstract_attack import AbstractAttack
from business_object.attack.attack_factory import AttackFactory


class AttackDao(metaclass=Singleton):
    def add_attack(self, attack: AbstractAttack) -> bool:
        """
        Add an attack to the database
        """
        created = False

        # Get the id type
        id_attack_type = TypeAttackDAO().find_id_by_label(attack.type)
        if id_attack_type is None:
            return created

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO tp.attack (id_attack_type, attack_name,        "
                    " power, accuracy, element, attack_description)             "
                    "VALUES                                                     "
                    "(%(id_attack_type)s, %(name)s, %(power)s, %(accuracy)s,    "
                    " %(element)s, %(description)s)                             "
                    "RETURNING id_attack;",
                    {
                        "id_attack_type": id_attack_type,
                        "name": attack.name,
                        "power": attack.power,
                        "accuracy": attack.accuracy,
                        "element": attack.element,
                        "description": attack.description,
                    },
                )
                res = cursor.fetchone()
        if res:
            attack.id = res["id_attack"]
            created = True

        return created

    def update_attack(self, attack: AbstractAttack) -> bool:
        updated = False

        # Get the id type
        id_type = TypeAttackDAO().find_id_by_label(attack.type)
        if id_type is None:
            return updated

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE tp.attack                                      "
                    "   SET attack_name = %(name)s,                        "
                    "       id_attack_type = %(id_type)s,                  "
                    "       power = %(power)s,                             "
                    "       accuracy = %(accuracy)s,                       "
                    "       element = %(element)s,                         "
                    "       attack_description = %(attack_description)s    "
                    " WHERE id_attack = %(id_attack)s                      ",
                    {
                        "id_type": id_type,
                        "name": attack.name,
                        "power": attack.power,
                        "accuracy": attack.accuracy,
                        "element": attack.element,
                        "attack_description": attack.description,
                        "id_attack": attack.id,
                    },
                )
                if cursor.rowcount:
                    updated = True
        return updated

    def find_attack_by_id(self, id_attack: int) -> Optional[AbstractAttack]:
        """
        Get an attack with a specific id. Return None if there is no attack

        :param attack_id: the attack id
        :type id_attack: int
        :return: the attack
        :rtype: Optional[AbstractAttack]
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *                                       "
                    "  FROM tp.attack                               "
                    "  JOIN tp.attack_type USING(id_attack_type)    "
                    " WHERE id_attack=%(id)s                        ",
                    {"id": id_attack},
                )
                res = cursor.fetchone()

        attack = None
        attack_factory = AttackFactory()

        if res:
            attack = attack_factory.instantiate_attack(
                type=res["attack_type_name"],
                id=res["id_attack"],
                power=res["power"],
                name=res["attack_name"],
                description=res["attack_description"],
                accuracy=res["accuracy"],
            )

        return attack

    def find_all_attacks(self, limit: int = 0, offest: int = 0) -> List[AbstractAttack]:
        """
        Get all attack in the db without any filter

        :param limit: how many attack are requested
        :type limit: int
        :param offest: the offset of the request
        :type offest: int
        """
        request = (
            "SELECT *                                        "
            "  FROM tp.attack                                "
            "  JOIN tp.attack_type USING(id_attack_type)     "
        )
        if limit:
            request += f" LIMIT {limit} "
        if offest:
            request += f" OFFSET {offest} "
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(request)
                res = cursor.fetchall()

        attacks = []
        attack_factory = AttackFactory()

        if res:
            for row in res:
                attack = attack_factory.instantiate_attack(
                    type=row["attack_type_name"],
                    id=row["id_attack"],
                    power=row["power"],
                    name=row["attack_name"],
                    description=row["attack_description"],
                    accuracy=row["accuracy"],
                )
                attacks.append(attack)

        return attacks

    def find_all_attacks_by_id_pokemon(self, id_pokemon: int) -> List[AbstractAttack]:
        """
        Get all attack of a specific pokemon with the given id

        :param id_pokemon: The pokemon id
        :type id_pokemon: int
        """
        request = (
            "SELECT *                                        "
            "  FROM tp.attack                                "
            "  JOIN tp.attack_type USING(id_attack_type)     "
            "  JOIN tp.pokemon_attack USING(id_attack)       "
            " WHERE id_pokemon=%(id_pokemon)s                "
        )

        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(request, {"id_pokemon": id_pokemon})
                res = cursor.fetchall()
        attacks = []
        attack_factory = AttackFactory()

        if res:
            for row in res:
                attack = attack_factory.instantiate_attack(
                    type=row["attack_type_name"],
                    id=row["id_attack"],
                    power=row["power"],
                    name=row["attack_name"],
                    description=row["attack_description"],
                    accuracy=row["accuracy"],
                )
                attacks.append(attack)
        return attacks


if __name__ == "__main__":
    # Pour charger les variables d'environnement contenues dans le fichier .env
    import dotenv
    from business_object.attack.physical_attack import PhysicalFormulaAttack

    dotenv.load_dotenv(override=True)

    # Création d'une attaque et ajout en BDD
    mon_attaque = PhysicalFormulaAttack(
        power=50,
        name="chatouille",
        description="guili-guilis",
        accuracy=90,
        element="Normal",
    )

    succes = AttackDao().add_attack(mon_attaque)
    print("Attack created in database : " + str(succes))
