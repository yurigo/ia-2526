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
dave = "Dave"
eve = "Eve"
frank = "Frank"
characters = [alice, bob, charlie, dave, eve, frank]

# Habitaciones
cocina = "Cocina"
salon = "Salon"
habitacion = "Habitacion"
banio = "Baño"
piscina= "piscina"
garage = "Garage"
rooms = [cocina, salon, habitacion, banio, piscina, garage]

# Armas
pistola = "Pistola"
candelabro = "Candelabro"
bate = "Bate"
movil = "Movil"
plancha = "plancha"
avion = "avion"
weapons = [pistola, candelabro, bate, movil, plancha, avion]

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
    ("OR", alice, bob, charlie, dave, eve, frank),
    # Al menos una habitación
    ("OR", cocina, salon, habitacion, banio, piscina, garage),
    # Al menos un arma
    ("OR", pistola, candelabro, bate, movil,plancha, avion),

)

# 2) Cartas iniciales que tenemos (NO pueden estar en el sobre)
# Sabemos que tenemos: Alice, Cocina y Pistola
knowledge = ("AND",
    knowledge,
    ("NOT", dave),
    ("NOT", piscina),
    ("NOT", pistola)
)



# 3) Información de otros jugadores
# Alguien nos mostró UNA de estas cartas (pero no sabemos cuál)
# Esto significa: Al menos una de {Bob, Salon, Candelabro} NO está en el sobre
knowledge = ("AND",
    knowledge,
    ("OR",
        ("NOT", bob),
        ("NOT", garage),
        ("NOT", pistola)
    )
)


knowledge = ("AND",
    knowledge,
    ("OR",
        ("NOT", charlie),
        ("NOT", habitacion),
        ("NOT", movil)
    )
)
knowledge = ("AND",
    knowledge,
    ("OR",
        ("NOT", frank),
        ("NOT", banio),
        ("NOT", plancha)
    )
)

knowledge = ("AND",
    knowledge,
    ("OR",
        ("NOT", eve),
        ("NOT", piscina),
        ("NOT", candelabro)
    )
)

knowledge = ("AND",
    knowledge,
    ("OR",
        ("NOT", alice),
        ("NOT", cocina),
        ("NOT", avion)
    )
)

knowledge = ("AND",
    knowledge,
    ("OR",
        ("NOT", frank),
        ("NOT", banio),
        ("NOT", bate)
    )
)

knowledge = ("AND",
    knowledge,
    ("OR",
        ("NOT", charlie),
        ("NOT", banio),
        ("NOT", bate)
    )
)
knowledge = ("AND",
    knowledge,
    ("OR",
        ("NOT", alice),
        ("NOT", banio),
        ("NOT", bate)
    )
)
knowledge = ("AND",
    knowledge,
    ("OR",
        ("NOT", bob),
        ("NOT", banio),
        ("NOT", bate)
    )
)
knowledge = ("AND",
    knowledge,
    ("OR",
        ("NOT", eve),
        ("NOT", banio),
        ("NOT", bate)
    )
)

knowledge = ("AND",
    knowledge,
    ("OR",
        ("NOT", alice),
        ("NOT", banio),
        ("NOT", bate)
    )
)
knowledge = ("AND",
    knowledge,
    ("OR",
        ("NOT", alice),
        ("NOT", salon),
        ("NOT", plancha)
    )
)


# 4) Más cartas conocidas que nos mostraron
# Sabemos que Charlie y Habitacion NO están en el sobre
knowledge = ("AND",
    knowledge,
    ("NOT", charlie),
    ("NOT", frank),
    ("NOT", dave),
    ("NOT", bob),
    ("NOT", eve),
    ("NOT", habitacion),
    ("NOT", cocina),
    ("NOT", plancha),
    ("NOT", candelabro),

)

knowledge = ("AND",
    knowledge,
    ("OR",
        ("NOT", bob),
        ("NOT", candelabro),
        ("NOT", habitacion)
    )
)

knowledge = ("AND",
    knowledge,
    ("OR",
        alice,
        ("NOT", cocina),
        ("NOT", plancha)
    )
)

print(show(knowledge))

# ----- VERIFICAR CONOCIMIENTO -----
print("\n🔍 RESOLVIENDO EL MISTERIO DE CLUEDO...")
check_knowledge(knowledge)


