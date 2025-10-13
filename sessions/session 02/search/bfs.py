# Breadth-first search (BFS)

from collections import deque


class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregar_arista(self, origen, destino, peso=1):
        if origen not in self.adyacencia:
            self.adyacencia[origen] = []
        self.adyacencia[origen].append((destino, peso))

    def obtener_sucesores(self, nodo):
        return self.adyacencia.get(nodo, [])


def bfs(grafo, inicio, objetivo):
    """
    Búsqueda en anchura (BFS - Breadth First Search)
    Explora por niveles usando una cola FIFO
    """
    visitados = set()
    cola = deque([(inicio, [inicio])])  # (nodo, camino)
    
    while cola:
        nodo, camino = cola.popleft()
        
        print(f"Visitando: {nodo}")
        
        if nodo == objetivo:
            print(f"¡Objetivo encontrado! Camino: {' -> '.join(camino)}")
            return True
        
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino, _ in grafo.obtener_sucesores(nodo):
                if vecino not in visitados:
                    cola.append((vecino, camino + [vecino]))
    
    return False


# Ejemplo de uso
g = Grafo()
g.agregar_arista('A', 'B', 1)
g.agregar_arista('A', 'C', 4)
g.agregar_arista('B', 'D', 2)
g.agregar_arista('B', 'E', 5)
g.agregar_arista('C', 'F', 1)
g.agregar_arista('E', 'F', 3)

print("=== Búsqueda BFS de A a F ===")
resultado = bfs(g, 'A', 'F')
if not resultado:
    print("No se encontró el objetivo")
