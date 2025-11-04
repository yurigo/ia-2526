"""
RAZONAMIENTO LÓGICO CON BACKTRACKING
====================================

Este script implementa un motor de inferencia lógica que determina si una base de 
conocimiento (KB) implica lógicamente una consulta (query) usando el algoritmo de 
backtracking para explorar todas las posibles asignaciones de valores de verdad.

¿CÓMO FUNCIONA EL ALGORITMO?
----------------------------

El algoritmo verifica si KB ⊨ query (KB implica query) mediante estos pasos:

1. EXTRACCIÓN DE SÍMBOLOS:
   Identifica todos los símbolos (variables proposicionales) que aparecen en KB y query.
   Ejemplo: si KB menciona "pikachu", "water", "squirtle", esos son los símbolos.

2. GENERACIÓN DE MODELOS (BACKTRACKING):
   Genera sistemáticamente todas las combinaciones posibles de valores True/False 
   para cada símbolo. Para n símbolos, hay 2^n modelos posibles.
   
   Ejemplo con 2 símbolos {A, B}:
   - Modelo 1: A=False, B=False
   - Modelo 2: A=False, B=True
   - Modelo 3: A=True, B=False
   - Modelo 4: A=True, B=True

3. VERIFICACIÓN DE LA IMPLICACIÓN:
   Para cada modelo completo, verifica la condición: (KB → query)
   Es decir: si KB es verdadera en ese modelo, entonces query también debe serlo.
   
   La implicación KB ⊨ query es VÁLIDA si y solo si:
   - En TODOS los modelos donde KB es verdadera, query también es verdadera.
   - Si encontramos un modelo donde KB=True pero query=False, retorna False.

EJEMPLO PRÁCTICO - BATALLA POKÉMON:
-----------------------------------

Base de conocimiento (KB):
- Regla 1: ¬water → pikachu    (Si no hay tipo agua, entonces es Pikachu)
- Regla 2a: pikachu ∨ squirtle  (Elegimos Pikachu o Squirtle)
- Regla 2b: ¬(pikachu ∧ squirtle) (No podemos usar ambos a la vez)
- Hecho 3: squirtle             (Usamos Squirtle)

Query: ¿water?  (¿El oponente es de tipo agua?)

El algoritmo explora todos los modelos:
- Si squirtle=True y pikachu=False:
  · De la Regla 1 (¬water → pikachu): si pikachu es False, water debe ser True
  · De la Regla 2a: se cumple (squirtle es True)
  · De la Regla 2b: se cumple (no usamos ambos)
  · De Hecho 3: se cumple (squirtle es True)
  → En todos los modelos consistentes con KB, water=True
  
Resultado: KB ⊨ water es VERDADERO

ESTRUCTURA DE EXPRESIONES LÓGICAS:
----------------------------------
- Variables simples: "pikachu", "water", etc.
- NOT: ("NOT", expr)
- AND: ("AND", expr1, expr2, ...)
- OR:  ("OR", expr1, expr2, ...)
- IMP: ("IMP", antecedente, consecuente)  →  p → q
- IFF: ("IFF", expr1, expr2)               →  p ↔ q

"""


# --- mismas funciones helpers ---
def symbols_in(expr):
    """Returns a set of all symbols in the logical expression."""
    if isinstance(expr, str):
        return {expr}
    op, *args = expr
    s = set()
    for a in args:
        s |= symbols_in(a)
    return s

def eval_expr(expr, model):
    """Evaluates the logical expression in the given model. """
    if isinstance(expr, str):
        return model[expr]
    op, *args = expr
    if op == "NOT": return not eval_expr(args[0], model)
    if op == "AND": return all(eval_expr(a, model) for a in args)
    if op == "OR":  return any(eval_expr(a, model) for a in args)
    if op == "IMP":
        p, q = args
        return (not eval_expr(p, model)) or eval_expr(q, model)
    if op == "IFF":
        p, q = args
        return eval_expr(p, model) == eval_expr(q, model)
    raise ValueError("Operador desconocido")

def entails(KB, query):
    """Returns True if KB entails query using backtracking."""
    syms = sorted(list(symbols_in(KB) | symbols_in(query)))
    model = {}

    def backtrack(i):
        # Si ya hay un modelo completo, comprobar condición: KB -> query
        if i == len(syms):
            return (not eval_expr(KB, model)) or eval_expr(query, model)

        sym = syms[i]

        # Probar sym = False
        model[sym] = False
        if not backtrack(i + 1):
            return False

        # Probar sym = True
        model[sym] = True
        if not backtrack(i + 1):
            return False

        # Limpieza (opcional)
        del model[sym]
        return True

    return backtrack(0)

# ----- Símbolos Pokémon -----
water = "water"
pikachu = "pikachu"
squirtle = "squirtle"

KB = ("AND",
        ("IMP", ("NOT", water), pikachu),    # 1) ¬water → pikachu
        ("OR", pikachu, squirtle),           # 2a) pikachu ∨ squirtle
        ("NOT", ("AND", pikachu, squirtle)), # 2b) no ambos
        squirtle                             # 3) se usó Squirtle
     )

query = water

print("¿KB ⊨ water?", entails(KB, query))  # Imprime: True


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

