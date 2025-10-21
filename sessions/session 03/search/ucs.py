import heapq

initialState = [
    [" ", "X", " ", " ", " "],
    [" ", "X", " ", "X", " "],
    [" ", " ", " ", "X", " "],
    ["X", "X", " ", " ", " "],
    [" ", " ", " ", "X", " "]
]

def valid_movement(state, nx, ny):
    filas = len(state)
    columnas = len(state[0])
    if not (0 <= nx < filas and 0 <= ny < columnas):
        return False
    if state[nx][ny] == "X":
        return False
    return True

def ucs(initialState, start, end):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    frontier = []
    heapq.heappush(frontier, (0, start, [start]))  # (coste_acumulado, nodo, camino)
    
    costos = {start: 0}

    while frontier:
        coste_actual, (x, y), camino = heapq.heappop(frontier)

        if (x, y) == end:
            return camino

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if valid_movement(initialState, nx, ny):
                nuevo_coste = coste_actual + 1  # costo uniforme para cada movimiento

                if (nx, ny) not in costos or nuevo_coste < costos[(nx, ny)]:
                    costos[(nx, ny)] = nuevo_coste
                    heapq.heappush(frontier, (nuevo_coste, (nx, ny), camino + [(nx, ny)]))

    return None

def print_labyrinth_with_path(labyrinth, path):
    labyrinth_copy = [row[:] for row in labyrinth]
    for x, y in path:
        if labyrinth_copy[x][y] == " ":
            labyrinth_copy[x][y] = "."
    for row in labyrinth_copy:
        print(" ".join(row))

start = (0, 0)
end = (4, 4)
path = ucs(initialState, start, end)

if path:
    print("Camino encontrado con UCS:")
    print(path)
    print("\nLaberinto con camino marcado:")
    print_labyrinth_with_path(initialState, path)
else:
    print("No se encontró un camino con UCS.")
