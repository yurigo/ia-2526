# backtracking search

def es_valido(solucion, nueva_opcion):
    """
    Verifica si la nueva opción es válida en el contexto de la solución actual.
    Para el problema de las N reinas: verifica que no haya conflictos.
    """
    fila_actual = len(solucion)
    for fila, columna in enumerate(solucion):
        # Misma columna
        if columna == nueva_opcion:
            return False
        # Misma diagonal
        if abs(columna - nueva_opcion) == abs(fila - fila_actual):
            return False
    return True


def backtrack(n, solucion=None, soluciones=None):
    """
    Backtracking para el problema de las N reinas.
    Coloca N reinas en un tablero de NxN sin que se ataquen entre sí.
    """
    if solucion is None:
        solucion = []
    if soluciones is None:
        soluciones = []
    
    # Caso base: solución completa
    if len(solucion) == n:
        soluciones.append(solucion[:])  # Copiar la solución
        return
    
    # Probar cada columna para la fila actual
    for columna in range(n):
        if es_valido(solucion, columna):
            # Añadir opción
            solucion.append(columna)
            # Recursión
            backtrack(n, solucion, soluciones)
            # Eliminar opción (backtrack)
            solucion.pop()
    
    return soluciones


def imprimir_tablero(solucion):
    """
    Imprime una solución del problema de las N reinas.
    """
    n = len(solucion)
    for fila in range(n):
        linea = []
        for columna in range(n):
            if solucion[fila] == columna:
                linea.append('♛')
            else:
                linea.append('·')
        print(' '.join(linea))
    print()


# Ejemplo de uso: resolver el problema de las 4 reinas
print("=== Problema de las 4 reinas (Backtracking) ===")
n = 4
soluciones = backtrack(n)

print(f"Se encontraron {len(soluciones)} soluciones:\n")
for i, sol in enumerate(soluciones, 1):
    print(f"Solución {i}: {sol}")
    imprimir_tablero(sol)
