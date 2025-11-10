"""
PUZZLE DE ASIGNACION POKEMON-POKEBALLS CON LOGICA PROPOSICIONAL
===============================================================

Este script resuelve un puzzle de asignación usando inferencia lógica.
Utiliza el módulo logic.py (versión con tuplas e itertools) para 
determinar qué Pokemon va con qué Pokeball.

PROBLEMA:
- Hay 4 Pokemon: Pikachu, Squirtle, Bulbasaur, Charmander
- Hay 4 Pokeballs: pokeball, greatball, ultraball, masterball
- Cada Pokemon debe estar en exactamente UNA Pokeball
- Cada Pokeball contiene exactamente UN Pokemon

REPRESENTACIÓN:
- Símbolo "PikachuPokeball" significa: "Pikachu está en una Pokeball normal"
- Símbolo "SquirtleGreatball" significa: "Squirtle está en una Greatball"

PISTAS:
- Pikachu está en Pokeball o Ultraball
- Squirtle NO está en Masterball
- Bulbasaur está en Ultraball
"""

from logic import *

pokemon = ["Pikachu", "Squirtle", "Bulbasaur", "Charmander"]
pokeballs = ["Pokeball", "Greatball", "Ultraball", "Masterball"]

# Generar todos los símbolos: PokemonPokeball
symbols = []
for poke in pokemon:
    for ball in pokeballs:
        symbols.append(f"{poke}{ball}")

# ----- BASE DE CONOCIMIENTO -----

# 1) REGLA: Cada Pokemon debe estar en ALGUNA Pokeball
reglas_pokemon_en_alguna_ball = []
for poke in pokemon:
    reglas_pokemon_en_alguna_ball.append(
        ("OR", f"{poke}Pokeball", f"{poke}Greatball", f"{poke}Ultraball", f"{poke}Masterball")
    )

knowledge = ("AND", *reglas_pokemon_en_alguna_ball)

# 2) REGLA: Cada Pokemon está en SOLO UNA Pokeball (no puede estar en dos)
reglas_una_ball_por_pokemon = []
for poke in pokemon:
    for b1 in pokeballs:
        for b2 in pokeballs:
            if b1 != b2:
                # Si Pokemon está en ball1, entonces NO está en ball2
                reglas_una_ball_por_pokemon.append(
                    ("IMP", f"{poke}{b1}", ("NOT", f"{poke}{b2}"))
                )

knowledge = ("AND", knowledge, *reglas_una_ball_por_pokemon)

# 3) REGLA: Cada Pokeball contiene SOLO UN Pokemon (no puede tener dos)
reglas_un_pokemon_por_ball = []
for ball in pokeballs:
    for p1 in pokemon:
        for p2 in pokemon:
            if p1 != p2:
                # Si Pokemon1 está en ball, entonces Pokemon2 NO está en ball
                reglas_un_pokemon_por_ball.append(
                    ("IMP", f"{p1}{ball}", ("NOT", f"{p2}{ball}"))
                )

knowledge = ("AND", knowledge, *reglas_un_pokemon_por_ball)

# 4) PISTA 1: Pikachu está en Pokeball o Ultraball
pista1 = ("OR", "PikachuPokeball", "PikachuUltraball")
knowledge = ("AND", knowledge, pista1)

# 5) PISTA 2: Squirtle NO está en Masterball
pista2 = ("NOT", "SquirtleMasterball")
knowledge = ("AND", knowledge, pista2)

# 6) PISTA 3: Bulbasaur está en Ultraball
pista3 = "BulbasaurUltraball"
knowledge = ("AND", knowledge, pista3)

print(show(knowledge))

# ----- RESOLVER Y MOSTRAR RESULTADO -----
print("\nRESOLVIENDO PUZZLE POKEMON-POKEBALLS...")
print("="*60)
print("\nPISTAS:")
print("  1. Pikachu está en Pokeball o Ultraball")
print("  2. Squirtle NO está en Masterball")
print("  3. Bulbasaur está en Ultraball")
print("\nANALIZANDO...")
print("-"*60)

asignaciones = {}
for symbol in symbols:
    if entails(knowledge, symbol):
        # Extraer pokemon y pokeball del símbolo
        # Ej: "PikachuPokeball" -> buscar donde termina el nombre del pokemon
        for poke in pokemon:
            if symbol.startswith(poke):
                ball = symbol[len(poke):]
                asignaciones[poke] = ball
                print(f"  {poke:12} -> {ball}")
                break

print("\nSOLUCION:")
print("="*60)
for poke in pokemon:
    if poke in asignaciones:
        print(f"  [{asignaciones[poke]:10}] : {poke}")
print("="*60)
