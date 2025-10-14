# Uniform cost search (UCS)

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


def ucs(grafo, inicio, objetivo):
    """
    Búsqueda de coste uniforme (UCS - Uniform Cost Search)
    Expande el nodo con menor coste acumulado usando una cola de prioridad
    """
    visitados = set()
    # Cola de prioridad: (coste_acumulado, nodo, camino)
    cola = [(0, inicio, [inicio])]
    g = {inicio: 0}  # Costes acumulados desde el inicio
    
    while cola:
        costo, nodo, camino = heapq.heappop(cola)
        
        print(f"Visitando: {nodo} (coste acumulado: {costo})")
        
        if nodo == objetivo:
            print(f"¡Objetivo encontrado! Camino: {' -> '.join(camino)}")
            print(f"Coste total: {costo}")
            return True
        
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino, peso in grafo.obtener_sucesores(nodo):
                if vecino not in visitados:
                    tentativo = g[nodo] + peso
                    if vecino not in g or tentativo < g[vecino]:
                        g[vecino] = tentativo
                        heapq.heappush(cola, (tentativo, vecino, camino + [vecino]))
    
    return False


# Ejemplo de uso
g = Grafo()
g.agregar_arista('A', 'B', 1)
g.agregar_arista('A', 'C', 4)
g.agregar_arista('B', 'D', 2)
g.agregar_arista('B', 'E', 5)
g.agregar_arista('C', 'F', 1)
g.agregar_arista('E', 'F', 3)

print("=== Búsqueda UCS de A a F ===")
resultado = ucs(g, 'A', 'F')
if not resultado:
    print("No se encontró el objetivo")
