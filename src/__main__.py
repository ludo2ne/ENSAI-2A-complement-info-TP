from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.pokemon.defender_pokemon import DefenderPokemon
from business_object.statistic import Statistic
from business_object.attack.special_attack import SpecialFormulaAttack
from business_object.attack.physical_attack import PhysicalFormulaAttack

from services.battle_service import BattleService

pikachu = AttackerPokemon(
    level=10,
    stat_current=Statistic(hp=100,
                           attack=60,
                           sp_atk=70,
                           defense=45,
                           sp_def=30,
                           speed=70),
    name="Pikachu",
    common_attacks=[
        PhysicalFormulaAttack(
            power=35,
            description="Pikachu fonce sur l'ennemi si rapidement qu'on parvient à peine à le discerner.",
            name="Vive attaque"
        ),
        SpecialFormulaAttack(
            power=30,
            description="Pikachu fait tomber la foudre sur son adversaire",
            name="Tonnerre"
        )]
)

snorlax = DefenderPokemon(
    level=10,
    stat_current=Statistic(hp=100,
                           attack=60,
                           sp_atk=40,
                           defense=60,
                           sp_def=50,
                           speed=40),
    name="Snorlax",
    common_attacks=[
        PhysicalFormulaAttack(
            power=30,
            description="Snorlax plaque le pokemon au sol",
            name="body_slam"
        )
    ]
)

print("Before battle")
print(pikachu)
print(snorlax)
print("-"*50)

battle = BattleService().resolve_battle(
    monstie_1=pikachu,
    monstie_2=snorlax
)

print(battle)
print("-"*50)


print("After battle")
print(pikachu)
print(snorlax)
