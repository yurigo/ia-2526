import heapq
import time

def generate_labyrinth_20x20():
    size = 20
    labyrinth = [["X"]*size for _ in range(size)]

    # Crear pasillo zigzagueante del inicio a fin con coste 1
    x, y = 0, 0
    labyrinth[x][y] = "1"
    while (x, y) != (size-1, size-1):
        if x < size-1 and (random.random() < 0.5 or y == size-1):
            x += 1
        elif y < size-1:
            y += 1
        labyrinth[x][y] = "1"

    # Rellenar otros sitios con pesos altos o bajos
    for i in range(size):
        for j in range(size):
            if labyrinth[i][j] != "1" and random.random() < 0.2:
                labyrinth[i][j] = str(random.choice([5, 8, 9]))
            elif labyrinth[i][j] != "1":
                labyrinth[i][j] = "X"

    labyrinth[0][0] = "1"
    labyrinth[size-1][size-1] = "1"
    return labyrinth

def print_labyrinth_with_path(labyrinth, path):
    labyrinth_copy = [row[:] for row in labyrinth]
    for x, y in path:
        if labyrinth_copy[x][y] != "X":
            labyrinth_copy[x][y] = "."
    for row in labyrinth_copy:
        print(" ".join(row))

def valid_movement(state, nx, ny):
    filas = len(state)
    columnas = len(state[0])
    if not (0 <= nx < filas and 0 <= ny < columnas):
        return False
    if state[nx][ny] == "X":
        return False
    return True

# DFS
def dfs(initialState, start, end):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    visitados = set([start])
    frontier = [(start, [start])]
    nodes_explored = 0

    while frontier:
        (x, y), camino = frontier.pop()
        nodes_explored += 1

        if (x, y) == end:
            return camino, nodes_explored

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if valid_movement(initialState, nx, ny) and (nx, ny) not in visitados:
                visitados.add((nx, ny))
                frontier.append(((nx, ny), camino + [(nx, ny)]))
    return None, nodes_explored

# BFS
from collections import deque
def bfs(initialState, start, end):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    visitados = set([start])
    frontier = deque([(start, [start])])
    nodes_explored = 0

    while frontier:
        (x, y), camino = frontier.popleft()
        nodes_explored += 1

        if (x, y) == end:
            return camino, nodes_explored

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if valid_movement(initialState, nx, ny) and (nx, ny) not in visitados:
                visitados.add((nx, ny))
                frontier.append(((nx, ny), camino + [(nx, ny)]))
    return None, nodes_explored

# UCS
def ucs(initialState, start, end):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    frontier = []
    heapq.heappush(frontier, (0, start, [start]))
    costos = {start: 0}
    nodes_explored = 0

    while frontier:
        coste_actual, (x, y), camino = heapq.heappop(frontier)
        nodes_explored += 1

        if (x, y) == end:
            return camino, nodes_explored

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if valid_movement(initialState, nx, ny):
                coste_celda = int(initialState[nx][ny])
                nuevo_coste = coste_actual + coste_celda

                if (nx, ny) not in costos or nuevo_coste < costos[(nx, ny)]:
                    costos[(nx, ny)] = nuevo_coste
                    heapq.heappush(frontier, (nuevo_coste, (nx, ny), camino + [(nx, ny)]))
    return None, nodes_explored

# A*
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(initialState, start, end):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    frontier = []
    heapq.heappush(frontier, (heuristic(start, end), 0, start, [start]))
    costos = {start: 0}
    nodes_explored = 0

    while frontier:
        f, coste_actual, (x, y), camino = heapq.heappop(frontier)
        nodes_explored += 1

        if (x, y) == end:
            return camino, nodes_explored

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if valid_movement(initialState, nx, ny):
                coste_celda = int(initialState[nx][ny])
                nuevo_coste = coste_actual + coste_celda

                if (nx, ny) not in costos or nuevo_coste < costos[(nx, ny)]:
                    costos[(nx, ny)] = nuevo_coste
                    f_nuevo = nuevo_coste + heuristic((nx, ny), end)
                    heapq.heappush(frontier, (f_nuevo, nuevo_coste, (nx, ny), camino + [(nx, ny)]))
    return None, nodes_explored

# MAIN
import random

random.seed(42)  # para reproducibilidad
labyrinth = generate_labyrinth_20x20()
print("Laberinto generado (20x20):")
print_labyrinth_with_path(labyrinth, [])

start = (0, 0)
end = (19, 19)

print("\nEjecutando DFS...")
path_dfs, nodes_dfs = dfs(labyrinth, start, end)
print(f"Nodos explorados por DFS: {nodes_dfs}")
if path_dfs:
    print(f"Camino DFS (longitud {len(path_dfs)}):")
    print(path_dfs)
else:
    print("No se encontró camino con DFS.")

print("\nEjecutando BFS...")
path_bfs, nodes_bfs = bfs(labyrinth, start, end)
print(f"Nodos explorados por BFS: {nodes_bfs}")
if path_bfs:
    print(f"Camino BFS (longitud {len(path_bfs)}):")
    print(path_bfs)
else:
    print("No se encontró camino con BFS.")

print("\nEjecutando UCS...")
path_ucs, nodes_ucs = ucs(labyrinth, start, end)
print(f"Nodos explorados por UCS: {nodes_ucs}")
if path_ucs:
    print(f"Camino UCS (longitud {len(path_ucs)}):")
    print(path_ucs)
else:
    print("No se encontró camino con UCS.")

print("\nEjecutando A*...")
path_astar, nodes_astar = a_star(labyrinth, start, end)
print(f"Nodos explorados por A*: {nodes_astar}")
if path_astar:
    print(f"Camino A* (longitud {len(path_astar)}):")
    print(path_astar)
else:
    print("No se encontró camino con A*.")

print("\nLaberinto con camino encontrado por A* marcado:")
print_labyrinth_with_path(labyrinth, path_astar)
