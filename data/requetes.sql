-- Toutes les attaques avec type
SELECT attack_type_name,
       a.*
  FROM tp.attack a
 INNER JOIN tp.attack_type t USING(id_attack_type)
 

-- Tous les pokemons avec type
SELECT pt.pokemon_type_name,
       p.*       
  FROM tp.pokemon p
 INNER JOIN tp.pokemon_type pt USING(id_pokemon_type) 
 
-- Toutes les attaques de Pikachu
SELECT a.*
  FROM tp.pokemon p
 INNER JOIN tp.pokemon_attack pa USING(id_pokemon)
 INNER JOIN tp.attack a USING(id_attack)
 WHERE name = 'Pikachu'
