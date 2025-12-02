import nltk

grammar = nltk.CFG.fromstring("""
    S  -> NP VP
    S  -> NP VP PP

    NP -> D N
    NP -> D Adj N
    NP -> D N Adj
    NP -> N
    NP -> PN
    NP -> NP PP

    VP -> V
    VP -> V NP
    VP -> V NP PP
    VP -> V PP

    PP -> P NP

    D   -> "el" | "la" | "los" | "las" | "un" | "una"
    N   -> "niño" | "niña" | "perro" | "coche" | "ciudad" | "pelota" | "parque"
    Adj -> "grande" | "pequeño" | "rojo" | "rápido"
    V   -> "vio" | "persiguió" | "condujo" | "llevó" | "encontró"
    P   -> "en" | "con" | "junto_a" | "a"
    PN  -> "juan" | "maria"
""")

parser = nltk.ChartParser(grammar)

print("Escribe la frase en minúsculas, separando las palabras por espacios.")
print("Ejemplos:")
print("  el perro vio la niña")
print("  el perro grande vio a la niña en el parque")
print("  juan condujo el coche rojo")
print("  la niña encontró la pelota en el parque")
print()

sentence = input("Frase: ").split()

try:
    parsed = False
    for tree in parser.parse(sentence):
        parsed = True
        print()
        tree.pretty_print()
        print(tree)  # versión lineal del árbol
    if not parsed:
        print("No se ha podido generar ningún árbol sintáctico para esa frase.")
except ValueError as e:
    print("Error al analizar la frase:", e)