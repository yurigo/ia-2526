import nltk

# Gramática mínima en castellano
grammar = nltk.CFG.fromstring("""
    S -> NP VP

    NP -> D N | N
    VP -> V | V NP

    D -> "el" | "la" | "un" | "una"
    N -> "niño" | "niña" | "ciudad" | "coche" | "perro"
    V -> "vio" | "persiguió" | "condujo"
""")

parser = nltk.ChartParser(grammar)

sentence = input("Frase: ").split()

try:
    for tree in parser.parse(sentence):
        print()
        tree.pretty_print()
except ValueError:
    print("No se puede generar un árbol sintáctico para esa frase.")