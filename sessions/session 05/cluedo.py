"""
RESOLVEDOR DE CLUEDO CON LÓGICA PROPOSICIONAL
=============================================

Este script resuelve un juego de Cluedo usando inferencia lógica.
Utiliza el módulo logic.py (versión con tuplas e itertools) para 
determinar qué cartas están en el sobre del crimen.

REGLAS DEL JUEGO:
- Hay 3 categorías: personajes, habitaciones y armas
- Una carta de cada categoría está en el sobre (la solución)
- El resto de cartas están repartidas entre los jugadores
- Debemos deducir qué cartas están en el sobre basándonos en:
  1. Cartas que tenemos (NO pueden estar en el sobre)
  2. Cartas que nos muestran otros jugadores (NO están en el sobre)
  3. Combinaciones que se descartan

REPRESENTACIÓN:
- Cada símbolo representa "esta carta está en el sobre"
- NOT(símbolo) significa "esta carta NO está en el sobre"
"""

from logic import *

# ----- Definir símbolos (cartas) -----
# Personajes
alice = "Alice"
bob = "Bob"
charlie = "Charlie"
characters = [alice, bob, charlie]

# Habitaciones
cocina = "Cocina"
salon = "Salon"
habitacion = "Habitacion"
rooms = [cocina, salon, habitacion]

# Armas
pistola = "Pistola"
candelabro = "Candelabro"
bate = "Bate"
weapons = [pistola, candelabro, bate]

# Todos los símbolos
symbols = characters + rooms + weapons


def check_knowledge(knowledge):
    """
    Verifica qué podemos deducir sobre cada carta.
    - YES (verde): Definitivamente está en el sobre
    - NO: Definitivamente NO está en el sobre
    - MAYBE: No estamos seguros
    """
    print("\n" + "="*50)
    print("ANÁLISIS DE CARTAS:")
    print("="*50)
    
    for symbol in symbols:
        # Verificar si KB ⊨ symbol (la carta ESTÁ en el sobre)
        if entails(knowledge, symbol):
            print(f"✓ {symbol}: SÍ está en el sobre")
        # Verificar si KB ⊨ NOT(symbol) (la carta NO está en el sobre)
        elif entails(knowledge, ("NOT", symbol)):
            print(f"✗ {symbol}: NO está en el sobre")
        else:
            print(f"? {symbol}: TAL VEZ")
    print("="*50 + "\n")


# ----- BASE DE CONOCIMIENTO -----

# 1) Regla fundamental: Debe haber exactamente UNA carta de cada categoría en el sobre
knowledge = ("AND",
    # Al menos un personaje
    ("OR", alice, bob, charlie),
    # Al menos una habitación
    ("OR", cocina, salon, habitacion),
    # Al menos un arma
    ("OR", pistola, candelabro, bate)
)

# 2) Cartas iniciales que tenemos (NO pueden estar en el sobre)
# Sabemos que tenemos: Alice, Cocina y Pistola
knowledge = ("AND",
    knowledge,
    ("NOT", alice),
    ("NOT", cocina),
    ("NOT", pistola)
)

# 3) Información de otros jugadores
# Alguien nos mostró UNA de estas cartas (pero no sabemos cuál)
# Esto significa: Al menos una de {Bob, Salon, Candelabro} NO está en el sobre
knowledge = ("AND",
    knowledge,
    ("OR",
        ("NOT", bob),
        ("NOT", salon),
        ("NOT", candelabro)
    )
)

# 4) Más cartas conocidas que nos mostraron
# Sabemos que Charlie y Habitacion NO están en el sobre
knowledge = ("AND",
    knowledge,
    ("NOT", charlie),
    ("NOT", habitacion)
)

# ----- VERIFICAR CONOCIMIENTO -----
print("\n🔍 RESOLVIENDO EL MISTERIO DE CLUEDO...")
check_knowledge(knowledge)

# ----- EXPLICACIÓN DE LA SOLUCIÓN -----
print("\n EXPLICACIÓN:")
print("-" * 50)
print("Cartas que TENEMOS (no están en el sobre):")
print("  - Alice, Cocina, Pistola")
print("\nCartas que nos MOSTRARON:")
print("  - Charlie, Habitacion")
print("  - Una de {Bob, Salon, Candelabro}")
print("\nPor eliminación:")
print("  - Personaje: Solo queda Bob (tenemos Alice, nos mostraron Charlie)")
print("  - Habitación: Solo queda Salon (tenemos Cocina, nos mostraron Habitacion)")
print("  - Arma: Solo queda Candelabro o Bate")
print("    * Si nos mostraron una de {Bob, Salon, Candelabro}")
print("    * Pero Bob y Salon ESTÁN en el sobre")
print("    * Entonces nos mostraron Candelabro")
print("    * Por lo tanto, el arma en el sobre debe ser: Bate")
print("\n SOLUCIÓN DEDUCIDA:")
print("  Personaje: Bob")
print("  Habitación: Salon")
print("  Arma: Bate")
print("="*50)


