initialState = [
    ["0", "X", "0", "0", "0"],
    ["0", "X", "0", "X", "0"],
    ["0", "0", "6", "X", "0"],
    ["X", "X", "6", "6", "0"],
    ["0", "0", "0", "X", "0"]
]

def valid_movement(state, nx, ny, visitados):
    filas = len(state)
    columnas = len(state[0])
    if not (0 <= nx < filas and 0 <= ny < columnas):
        return False
    if state[nx][ny] == "X":
        return False
    if (nx, ny) in visitados:
        return False
    return True

def dfs(initialState, start, end):
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    visitados = [start]
    frontier = [(start, [start])]

    while frontier:
        (x, y), camino = frontier.pop()
        if (x, y) == end:
            return camino
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if valid_movement(initialState, nx, ny, visitados):
                visitados.append((nx, ny))
                frontier.append(((nx, ny), camino + [(nx, ny)]))
    return None  # No se encontró camino

def print_labyrinth_with_path(labyrinth, path):
    labyrinth_copy = [row[:] for row in labyrinth]
    for x, y in path:
        if labyrinth_copy[x][y] == " ":
            labyrinth_copy[x][y] = "."
    for row in labyrinth_copy:
        print(" ".join(row))

start = (0, 0)
end = (4, 4)
path = dfs(initialState, start, end)

def calculateCost(state, path):
    total = 0
    for x, y in path:
        total += int(state[x][y])  # suma el coste convertido a entero
    return total

if path:
    print("Camino encontrado:")
    print(path)
    print("Coste total:", calculateCost(initialState, path)
    print("\nLaberinto con camino marcado:")
    print_labyrinth_with_path(initialState, path)
else:
    print("No se encontró un camino.")
