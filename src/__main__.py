
from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.pokemon.defender_pokemon import DefenderPokemon
from business_object.statistic import Statistic
from business_object.attack.special_attack import SpecialFormulaAttack
from business_object.attack.physical_attack import PhysicalFormulaAttack

from services.battle_service import BattleService

# Cr

pikachu = AttackerPokemon(
    level=10,
    stat_current=Statistic(hp=100,
                           attack=60,
                           sp_atk=70,
                           defense=40,
                           sp_def=30,
                           speed=70),
    name="pikachu",
    common_attacks=[
        PhysicalFormulaAttack(
            power=35,
            description="{pokemon} fonce sur l'ennemi si rapidement qu'on parvient à peine à le discerner.",
            name="Vive attaque"
        ),
        SpecialFormulaAttack(
            power=30,
            description="{pokemon} fait tomber la foudre sur son adversaire",
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
            description="{pokemon} plaque le pokemon au sol",
            name="body_slam"
        )
    ]
)

print("Before battle")
print(pikachu)
print(snorlax)
print("-"*50)

BattleService().resolve_battle(
    monstie_1=pikachu,
    monstie_2=snorlax
)


print("After battle")
print(pikachu)
print(snorlax)
