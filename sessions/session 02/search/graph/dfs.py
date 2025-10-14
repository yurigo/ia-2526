# Depth-first search (DFS)

class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregar_arista(self, origen, destino, peso=1):
        if origen not in self.adyacencia:
            self.adyacencia[origen] = []
        self.adyacencia[origen].append((destino, peso))

    def obtener_sucesores(self, nodo):
        return self.adyacencia.get(nodo, [])


def dfs(grafo, inicio, objetivo, visitados=None, camino=None):
    """
    Búsqueda en profundidad (DFS - Depth First Search)
    Explora en profundidad antes de retroceder
    """
    if visitados is None:
        visitados = set()
    if camino is None:
        camino = []
    
    visitados.add(inicio)
    camino.append(inicio)
    
    print(f"Visitando: {inicio}")
    
    if inicio == objetivo:
        print(f"¡Objetivo encontrado! Camino: {' -> '.join(camino)}")
        return True
    
    for vecino, _ in grafo.obtener_sucesores(inicio):
        if vecino not in visitados:
            if dfs(grafo, vecino, objetivo, visitados, camino):
                return True
    
    camino.pop()  # Backtrack
    return False


# Ejemplo de uso
g = Grafo()
g.agregar_arista('A', 'B', 1)
g.agregar_arista('A', 'C', 4)
g.agregar_arista('B', 'D', 2)
g.agregar_arista('B', 'E', 5)
g.agregar_arista('C', 'F', 1)
g.agregar_arista('E', 'F', 3)

print("=== Búsqueda DFS de A a F ===")
resultado = dfs(g, 'A', 'F')
if not resultado:
    print("No se encontró el objetivo")
