DROP SCHEMA IF EXISTS tp CASCADE;
CREATE SCHEMA tp;

--------------------------------------------------------------
-- Types d Attaques
--------------------------------------------------------------

DROP TABLE IF EXISTS tp.attack_type CASCADE ;
CREATE TABLE tp.attack_type (
    id_attack_type serial PRIMARY KEY,
    attack_type_name text UNIQUE NOT NULL,
    attack_type_description text NOT NULL
);


--------------------------------------------------------------
-- Attaques
--------------------------------------------------------------

DROP TABLE IF EXISTS tp.attack;

CREATE TABLE tp.attack (
    id_attack SERIAL PRIMARY KEY,
    id_attack_type integer REFERENCES tp.attack_type(id_attack_type),
    power integer,
    accuracy integer,
    element text,
    attack_name text UNIQUE NOT NULL,
    attack_description text
);


--------------------------------------------------------------
-- Types de Pokemons
--------------------------------------------------------------

DROP TABLE IF EXISTS tp.pokemon_type CASCADE ;

CREATE TABLE tp.pokemon_type (
    id_pokemon_type serial PRIMARY KEY,
    pokemon_type_name text UNIQUE NOT NULL,
    pokemon_type_description text
);


--------------------------------------------------------------
-- Pokemons
--------------------------------------------------------------

DROP TABLE IF EXISTS tp.pokemon CASCADE;

CREATE TABLE tp.pokemon (
    id_pokemon_type integer REFERENCES tp.pokemon_type(id_pokemon_type),
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

-- Comme on va creer des pokemon en forcant les id_pokemon
-- il faut maj a la main la valeur de la sequence de la PK
ALTER SEQUENCE tp.pokemon_id_pokemon_seq RESTART WITH 899;


--------------------------------------------------------------
-- Attaques des Pokemons
--------------------------------------------------------------

DROP TABLE IF EXISTS tp.pokemon_attack CASCADE;

CREATE TABLE tp.pokemon_attack (
    id_pokemon integer REFERENCES tp.pokemon(id_pokemon) ON DELETE CASCADE,
    id_attack integer REFERENCES tp.attack(id_attack) ON DELETE CASCADE,
    level integer,
    PRIMARY KEY (id_pokemon, id_attack)
);