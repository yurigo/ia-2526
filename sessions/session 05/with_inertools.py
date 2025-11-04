"""
RAZONAMIENTO LÓGICO CON ITERTOOLS (VERSIÓN MEJORADA)
====================================================

Este script resuelve el mismo problema de inferencia lógica que basic.py, pero 
importa la lógica desde un módulo externo (logic.py) que usa itertools.product()
en lugar de backtracking manual.

¿CÓMO FUNCIONA LA VERSIÓN CON ITERTOOLS?
----------------------------------------

La función entails() en logic.py utiliza itertools.product() para generar todas 
las combinaciones posibles de valores True/False de forma más eficiente:

    from itertools import product
    
    def entails(KB, query):
        syms = sorted(list(symbols_in(KB) | symbols_in(query)))
        
        # product([False, True], repeat=n) genera todas las 2^n combinaciones
        for vals in product([False, True], repeat=len(syms)):
            model = dict(zip(syms, vals))
            
            # Solo verifica modelos donde KB es verdadera
            if eval_expr(KB, model):
                if not eval_expr(query, model):
                    return False  # Contraejemplo encontrado
        return True

EJEMPLO: Con 3 símbolos {pikachu, squirtle, water}
product([False, True], repeat=3) genera automáticamente:
    (False, False, False)
    (False, False, True)
    (False, True, False)
    (False, True, True)
    (True, False, False)
    (True, False, True)
    (True, True, False)
    (True, True, True)

Luego zip() asocia cada tupla con los símbolos:
    {pikachu: False, squirtle: False, water: False}
    {pikachu: False, squirtle: False, water: True}
    ... etc.

¿POR QUÉ ES MEJOR LA VERSIÓN CON ITERTOOLS?
-------------------------------------------

1. CÓDIGO MÁS LIMPIO Y LEGIBLE:
   - No necesita funciones recursivas anidadas (backtrack)
   - Menos líneas de código (≈10 líneas vs ≈20 en basic.py)
   - La intención es más clara: "para cada combinación posible..."

2. MENOS PROPENSO A ERRORES:
   - No hay que gestionar manualmente el estado del modelo (agregar/eliminar símbolos)
   - No hay riesgo de olvidar limpiar el modelo después de backtrack
   - itertools.product() es una función probada y optimizada

3. MÁS PITÓNICO:
   - Usa herramientas estándar de Python (itertools)
   - Aprovecha el poder de los iteradores
   - Sigue el principio de "usar bibliotecas en lugar de reinventar"

4. SEPARACIÓN DE RESPONSABILIDADES:
   - La lógica está en un módulo separado (logic.py)
   - Este archivo solo contiene los casos de uso (KB y queries)
   - Más fácil de mantener y reutilizar

5. MISMO RENDIMIENTO, MEJOR MANTENIBILIDAD:
   - Ambos exploran 2^n modelos (misma complejidad temporal)
   - Pero itertools es más eficiente en memoria (generador perezoso)
   - Más fácil de entender para otros programadores

EJEMPLO PRÁCTICO - BATALLA POKÉMON:
-----------------------------------
(Ver basic.py para la explicación detallada del razonamiento lógico)

Base de conocimiento:
- ¬water → pikachu
- pikachu ∨ squirtle
- ¬(pikachu ∧ squirtle)
- squirtle (hecho)

Query: water

El algoritmo con itertools genera todas las combinaciones y verifica:
→ En todos los modelos donde KB=True, ¿es water=True?
→ Resultado: Sí, KB ⊨ water es VERDADERO

"""


from logic import *

# ----- Símbolos Pokémon -----
water = "water"
pikachu = "pikachu"
squirtle = "squirtle"

KB = ("AND",
        ("IMP", ("NOT", water), pikachu),               # 1) ¬water → pikachu
        ("OR", pikachu, squirtle),                      # 2a) pikachu ∨ squirtle
        ("NOT", ("AND", pikachu, squirtle)),            # 2b) no ambos
        squirtle                                        # 3) se usó Squirtle
     )

query = water

print("¿KB ⊨ water?", entails(KB, query))  # Debe imprimir: True


# ---- Otro ejemplo ----

# ----- Símbolos -----
water = "water"          # el oponente es de tipo agua
electric = "electric"    # el Pokémon es de tipo eléctrico
pikachu = "pikachu"
squirtle = "squirtle"
thunder = "thunder"      # se usó ataque trueno
win = "win"              # se gana la batalla
lose = "lose"            # se pierde la batalla
same_type = "same_type"  # ambos son del mismo tipo

# ----- Base de conocimiento -----
KB = ("AND",
    ("IMP", pikachu, electric),                # Pikachu es de tipo eléctrico
    ("IMP", squirtle, water),                  # Squirtle es de tipo agua
    ("IMP", thunder, electric),                # Usar Thunder implica tipo eléctrico
    ("IMP", ("AND", electric, water), win),    # Eléctrico vence a Agua
    ("IMP", ("AND", water, electric), lose),   # Agua pierde contra Eléctrico
    ("IMP", ("AND", pikachu, thunder), win),   # Pikachu usa Thunder → gana
    ("IMP", ("AND", squirtle, electric), lose),# Squirtle vs Eléctrico → pierde
    ("IMP", ("AND", squirtle, ("NOT", electric)), win), # Squirtle gana si el rival no es eléctrico
    ("IMP", ("AND", pikachu, squirtle), ("NOT", same_type)), # No son del mismo tipo
    squirtle                                     # hecho: se usó Squirtle
)

query = win
print("¿KB ⊨ win?", entails(KB, query))

query = ("AND", pikachu, win)
print("¿KB ⊨ Pikachu gana?", entails(KB, query))

query = same_type
print("¿KB ⊨ same_type?", entails(KB, query))

query = water
print("¿KB ⊨ water?", entails(KB, query))
