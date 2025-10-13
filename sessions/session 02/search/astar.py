# A* search (A*)

import heapq


class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregar_arista(self, origen, destino, peso=1):
        if origen not in self.adyacencia:
            self.adyacencia[origen] = []
        self.adyacencia[origen].append((destino, peso))

    def obtener_sucesores(self, nodo):
        return self.adyacencia.get(nodo, [])


def a_star(grafo, inicio, objetivo, heuristica):
    """
    Búsqueda A* (A Star)
    Combina coste real g(n) y heurística h(n): f(n) = g(n) + h(n)
    Expande el nodo con menor f(n) estimado
    """
    visitados = set()
    # Cola de prioridad: (f, nodo, camino, coste_g)
    cola = [(heuristica(inicio), inicio, [inicio], 0)]
    g = {inicio: 0}  # Costes reales desde el inicio
    
    while cola:
        f, nodo, camino, costo_g = heapq.heappop(cola)
        
        print(f"Visitando: {nodo} (g={costo_g}, h={heuristica(nodo)}, f={f})")
        
        if nodo == objetivo:
            print(f"¡Objetivo encontrado! Camino: {' -> '.join(camino)}")
            print(f"Coste total: {costo_g}")
            return True
        
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino, peso in grafo.obtener_sucesores(nodo):
                if vecino not in visitados:
                    tentativo_g = g[nodo] + peso
                    if vecino not in g or tentativo_g < g[vecino]:
                        g[vecino] = tentativo_g
                        f_vecino = tentativo_g + heuristica(vecino)
                        heapq.heappush(cola, (f_vecino, vecino, camino + [vecino], tentativo_g))
    
    return False


# Ejemplo de uso con heurística simple
# Heurística: estimación de distancia al objetivo
# En este ejemplo, usamos valores ficticios para ilustrar
heuristicas = {
    'A': 5,
    'B': 4,
    'C': 2,
    'D': 4,
    'E': 2,
    'F': 0  # objetivo
}

def heuristica(nodo):
    return heuristicas.get(nodo, 0)


g = Grafo()
g.agregar_arista('A', 'B', 1)
g.agregar_arista('A', 'C', 4)
g.agregar_arista('B', 'D', 2)
g.agregar_arista('B', 'E', 5)
g.agregar_arista('C', 'F', 1)
g.agregar_arista('E', 'F', 3)

print("=== Búsqueda A* de A a F ===")
resultado = a_star(g, 'A', 'F', heuristica)
if not resultado:
    print("No se encontró el objetivo")
