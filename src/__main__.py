from business_object.pokemon.pokemon import Pokemon
from business_object.statistic import Statistic

# Create statistics for the following pokemon
stats_pk1 = Statistic(100, 40, 10, 10, 10, 10)

# Create a pokemon
pk1 = Pokemon(name="pika", stat_current=stats_pk1, type_pk="Attacker")

# Print the pokemon (call __str__() method)
print(pk1)
