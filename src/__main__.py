
from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.statistic import Statistic

# Create statistics for the following pokemon
stats_pk1 = Statistic(100, 40, 10, 10, 10, 10)

# Create a pokemon
pk1 = AttackerPokemon(name='pika',
                      stat_current=stats_pk1)

# Increase level
pk1.level_up()

# Print the pokemon (call __str__() method)
print(pk1)
