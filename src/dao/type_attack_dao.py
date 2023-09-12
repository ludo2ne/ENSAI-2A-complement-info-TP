from typing import List, Optional
from dao.db_connection import DBConnection
from utils.singleton import Singleton


class TypeAttackDAO(metaclass=Singleton):
    """
    Communicate with the attack_type table
    """

    def find_all_attack_type(self) -> List[str]:
        """
        Get all attack type names and return a list

        :return: A list of all types
        :rtype: List of str
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT *                                  "
                    "  FROM tp.attack_type                     "
                )

                # to store raw results
                res = cursor.fetchall()

        # Create an empty list to store formatted results
        type_attack: List[str] = []

        # if the SQL query returned results (ie. res not None)
        if res:
            for row in res:
                type_attack.append(row["attack_type_name"])

                print(row["id_attack_type"])
                print(row["attack_type_name"])
                print(row["attack_type_description"])

        return type_attack

    def find_id_by_label(self, label: str) -> Optional[int]:
        """
        Get the id_attack_type from the label
        """
        with DBConnection().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT id_attack_type                     "
                    "  FROM tp.attack_type                     "
                    " WHERE attack_type_name = %(attack_name)s ",
                    {"attack_name": label},
                )
                res = cursor.fetchone()

        if res:
            return res["id_attack_type"]


if __name__ == "__main__":
    # Pour charger les variables d'environnement contenues dans le fichier .env
    import dotenv

    dotenv.load_dotenv(override=True)

    attack_types = TypeAttackDAO().find_all_attack_type()
    print(attack_types)
