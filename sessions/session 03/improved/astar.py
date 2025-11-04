import heapq
import math
import random

def generate_labyrinth_20x20():
    size = 100
    labyrinth = [["X"]*size for _ in range(size)]

    # Crear pasillo zigzagueante del inicio a fin con coste 1
    x, y = 0, 0
    labyrinth[x][y] = "1"
    while (x, y) != (size-1, size-1):
        if x < size-1 and (random.random() < 0.9 or y == size-1):
            x += 1
        elif y < size-1:
            y += 1
        labyrinth[x][y] = "1"

    # Rellenar otros sitios con pesos altos o bajos
    for i in range(size):
        for j in range(size):
            # if i == j:
            #     labyrinth[i][j] = 1
            #     continue
            if labyrinth[i][j] != "1" and random.random() < 0.7:
                labyrinth[i][j] = str(random.choice([1,5,9]))
            elif labyrinth[i][j] != "1":
                labyrinth[i][j] = "X"

    labyrinth[0][0] = "1"
    labyrinth[size-1][size-1] = "1"
    return labyrinth


# initialState = [
#     ["1", "X", "1", "1", "1", "1", "X", "1", "1", "1"], 
#     ["1", "X", "1", "1", "X", "1", "X", "1", "X", "1"], 
#     ["1", "1", "1", "6", "X", "1", "1", "1", "X", "1"], 
#     ["X", "X", "1", "6", "6", "1", "X", "1", "X", "1"], 
#     ["1", "1", "1", "6", "X", "1", "X", "1", "X", "1"],
#     ["1", "1", "1", "6", "X", "1", "X", "1", "X", "1"],
#     ["1", "1", "1", "6", "X", "1", "X", "1", "X", "1"],
#     ["1", "1", "1", "6", "1", "1", "X", "1", "X", "1"],
#     ["1", "1", "1", "6", "X", "1", "X", "1", "X", "1"],
#     ["1", "1", "1", "6", "X", "1", "X", "1", "X", "1"],
#     ["1", "1", "1", "6", "X", "1", "1", "1", "X", "1"],
#     ["1", "1", "1", "6", "X", "1", "X", "1", "X", "1"],
#     ["1", "1", "1", "6", "X", "1", "X", "1", "X", "1"],
#     ["1", "1", "1", "6", "X", "1", "1", "1", "1", "1"],
#     ["1", "1", "1", "1", "1", "1", "X", "1", "X", "1"]
# ]

initialState = generate_labyrinth_20x20()

visitados=[]
consultados=[]

def valid_movement(state, nx, ny):
    filas = len(state)
    columnas = len(state[0])
    if not (0 <= nx < filas and 0 <= ny < columnas):
        return False
    if state[nx][ny] == "X":
        return False
    return True

def heuristic(a, b):
    # Distancia Manhattan
    # return abs(a[0] - b[0]) + abs(a[1] - b[1])
    # distancia euclidiana
    return math.sqrt((a[0] - b[0])**2 + + (a[1] - b[1])**2)

def a_star(initialState, start, end):
    directions = [(1,0), (-1,0), (0,1), (0,-1), 
                  (1,1), (-1,1) , (1,-1), (-1,-1)]

    frontier = []
    heapq.heappush(frontier, (0 + heuristic(start, end), 0, start, [start]))  
    # (f = g + h, g, nodo, camino)
    
    costos = {start: 0}

    while frontier:
        f, coste_actual, (x, y), camino = heapq.heappop(frontier)

        if (x, y) == end:
            return camino

        visitados.append((x,y))
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if valid_movement(initialState, nx, ny):
                coste_del_movimiento = math.sqrt((nx - x)**2 + + (ny - y)**2)
                coste_celda = int(initialState[nx][ny])
                nuevo_coste = coste_actual + coste_celda + coste_del_movimiento
                consultados.append((nx,ny))
                if (nx, ny) not in costos or nuevo_coste < costos[(nx, ny)]:
                    costos[(nx, ny)] = nuevo_coste
                    f_nuevo = nuevo_coste + heuristic((nx, ny), end)
                    heapq.heappush(frontier, (f_nuevo, nuevo_coste, (nx, ny), camino + [(nx, ny)]))

    return None

def calculateCost(state, path):
    total = 0
    for x, y in path:
        total += int(state[x][y])  # suma el coste convertido a entero
    return total

def print_labyrinth_with_path(labyrinth, path):
    labyrinth_copy = [row[:] for row in labyrinth]
    for x, y in consultados:
        labyrinth_copy[x][y] = "*"
    for x, y in visitados:
        labyrinth_copy[x][y] = "-"
    for x, y in path:
        if labyrinth_copy[x][y] != "X":
            labyrinth_copy[x][y] = "."
    for row in labyrinth_copy:
        print(" ".join(row))

start = (0, 0)
end = (99, 99)
path = a_star(initialState, start, end)

if path:
    print("Camino encontrado con A*:")
    print(path)
    print("Visitados: ")
    print(visitados)
    print("Coste total:", calculateCost(initialState, path))
    print("\nLaberinto con camino marcado:")
    print_labyrinth_with_path(initialState, path)
else:
    print("No se encontró un camino con A*.")