DROP SCHEMA IF EXISTS tp_pokemon CASCADE;
CREATE SCHEMA tp_pokemon;

--------------------------------------------------------------

DROP TABLE IF EXISTS tp_pokemon.attack_type CASCADE ;
CREATE TABLE tp_pokemon.attack_type (
    id_attack_type serial PRIMARY KEY,
    attack_type_name text UNIQUE NOT NULL,
    attack_type_description text NOT NULL
);

--------------------------------------------------------------

DROP TABLE IF EXISTS tp_pokemon.attack;

CREATE TABLE tp_pokemon.attack (
    id_attack SERIAL PRIMARY KEY,
    id_attack_type integer REFERENCES attack_type(id_attack_type),
    power integer,
    accuracy integer,
    element text,
    attack_name text UNIQUE NOT NULL,
    attack_description text
);

--------------------------------------------------------------

DROP TABLE IF EXISTS tp_pokemon.pokemon_type CASCADE ;

CREATE TABLE tp_pokemon.pokemon_type (
id_type_pokemon serial PRIMARY KEY,
pokemon_type_name text UNIQUE NOT NULL,
pokemon_type_description text
);

--------------------------------------------------------------

DROP TABLE IF EXISTS tp_pokemon.pokemon CASCADE;

CREATE TABLE tp_pokemon.pokemon (
    id_pokemon_type integer REFERENCES pokemon_type(id_type_pokemon),
    name text UNIQUE NOT NULL,
    id_pokemon serial PRIMARY KEY,
    level integer,
    hp integer,
    attack integer,
    defense integer,
    spe_atk integer,
    spe_def integer,
    speed integer,
    url_image text
);


--------------------------------------------------------------


DROP TABLE IF EXISTS tp_pokemon.pokemon_attack CASCADE;

CREATE TABLE tp_pokemon.pokemon_attack (
    id_pokemon integer REFERENCES pokemon(id_pokemon) ON DELETE CASCADE,
    id_attack integer REFERENCES attack(id_attack) ON DELETE CASCADE,
    level integer,
    PRIMARY KEY (id_pokemon, id_attack)
);