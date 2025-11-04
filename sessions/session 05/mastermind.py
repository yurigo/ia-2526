"""
RESOLVEDOR DE MASTERMIND CON LÓGICA PROPOSICIONAL
=================================================

Este script resuelve un juego de Mastermind usando inferencia lógica.
Utiliza el módulo logic.py (versión con tuplas e itertools) para 
determinar la combinación secreta de colores.

REGLAS DEL JUEGO:
- Hay 4 posiciones: 0, 1, 2, 3
- Cada posición tiene un color: red, blue, green, yellow
- Cada color aparece exactamente UNA vez
- Basándonos en pistas (número de colores en posición correcta),
  debemos deducir la combinación exacta

REPRESENTACIÓN:
- Símbolo "red0" significa: "el color rojo está en la posición 0"
- Símbolo "blue2" significa: "el color azul está en la posición 2"

PISTAS DEL EJEMPLO:
- Pista 1: Exactamente 2 colores están en posición correcta
  (entre red0, blue1, green2, yellow3)
- Pista 2: Estas posiciones son INCORRECTAS: blue0, red1, green2, yellow3
"""

from logic import *

colors = ["red", "blue", "green", "yellow"]

# Generar todos los símbolos: color0, color1, color2, color3
symbols = []
for i in range(4):
    for color in colors:
        symbols.append(f"{color}{i}")

# ----- BASE DE CONOCIMIENTO -----

# 1) REGLA: Cada color debe estar en ALGUNA posición
reglas_color_en_alguna_posicion = []
for color in colors:
    reglas_color_en_alguna_posicion.append(
        ("OR", f"{color}0", f"{color}1", f"{color}2", f"{color}3")
    )

knowledge = ("AND", *reglas_color_en_alguna_posicion)

# 2) REGLA: Cada color está en SOLO UNA posición (no puede estar en dos posiciones)
reglas_unica_posicion = []
for color in colors:
    for i in range(4):
        for j in range(4):
            if i != j:
                # Si color está en posición i, entonces NO está en posición j
                reglas_unica_posicion.append(
                    ("IMP", f"{color}{i}", ("NOT", f"{color}{j}"))
                )

knowledge = ("AND", knowledge, *reglas_unica_posicion)

# 3) REGLA: Cada posición tiene SOLO UN color (no puede tener dos colores)
reglas_un_color_por_posicion = []
for i in range(4):
    for c1 in colors:
        for c2 in colors:
            if c1 != c2:
                # Si c1 está en posición i, entonces c2 NO está en posición i
                reglas_un_color_por_posicion.append(
                    ("IMP", f"{c1}{i}", ("NOT", f"{c2}{i}"))
                )

knowledge = ("AND", knowledge, *reglas_un_color_por_posicion)

# 4) PISTA 1: Exactamente 2 colores están en posición correcta
# Las combinaciones posibles de 2 correctos de {red0, blue1, green2, yellow3}:
pista1 = ("OR",
    # red0 y blue1 correctos (green2 y yellow3 incorrectos)
    ("AND", "red0", "blue1", ("NOT", "green2"), ("NOT", "yellow3")),
    # red0 y green2 correctos
    ("AND", "red0", "green2", ("NOT", "blue1"), ("NOT", "yellow3")),
    # red0 y yellow3 correctos
    ("AND", "red0", "yellow3", ("NOT", "blue1"), ("NOT", "green2")),
    # blue1 y green2 correctos
    ("AND", "blue1", "green2", ("NOT", "red0"), ("NOT", "yellow3")),
    # blue1 y yellow3 correctos
    ("AND", "blue1", "yellow3", ("NOT", "red0"), ("NOT", "green2")),
    # green2 y yellow3 correctos
    ("AND", "green2", "yellow3", ("NOT", "red0"), ("NOT", "blue1"))
)

knowledge = ("AND", knowledge, pista1)

# 5) PISTA 2: Estas posiciones son INCORRECTAS
pista2 = ("AND",
    ("NOT", "blue0"),
    ("NOT", "red1"),
    ("NOT", "green2"),
    ("NOT", "yellow3")
)

knowledge = ("AND", knowledge, pista2)

# ----- RESOLVER Y MOSTRAR RESULTADO -----
print("\nRESOLVIENDO MASTERMIND...")
print("="*50)
print("\nPISTAS:")
print("  1. Exactamente 2 de {red0, blue1, green2, yellow3} son correctos")
print("  2. Estas posiciones son INCORRECTAS: blue0, red1, green2, yellow3")
print("\nANALIZANDO...")
print("-"*50)

solucion = {}
for i in range(4):
    solucion[i] = None

for symbol in symbols:
    if entails(knowledge, symbol):
        # Extraer color y posición del símbolo (ej: "red0" -> color="red", pos=0)
        color = symbol[:-1]
        posicion = int(symbol[-1])
        solucion[posicion] = color
        print(f"✓ Posición {posicion}: {color.upper()}")

print("\nSOLUCION:")
print("="*50)
resultado = " | ".join([f"[{i}]: {solucion[i].upper()}" for i in range(4) if solucion[i]])
print(f"  {resultado}")
print("="*50)

print("\nEXPLICACION:")
print("-"*50)
print("De la pista 2 sabemos que:")
print("  - blue NO está en posición 0")
print("  - red NO está en posición 1")
print("  - green NO está en posición 2")
print("  - yellow NO está en posición 3")
print("\nDe la pista 1 (exactamente 2 de {red0, blue1, green2, yellow3}):")
print("  - Como green2 y yellow3 son INCORRECTAS (pista 2)")
print("  - Solo quedan red0 y blue1 como posibles correctos")
print("  - Por lo tanto: red está en posición 0 y blue está en posición 1")
print("\nPor eliminación:")
print("  - Las posiciones 2 y 3 deben tener green y yellow")
print("  - Como green NO puede estar en posición 2 → green en posición 3")
print("  - Como yellow NO puede estar en posición 3 → yellow en posición 2")
print("\nSolución deducida correctamente!")
print("="*50)
