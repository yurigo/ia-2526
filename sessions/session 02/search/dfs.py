# Depth-first search (DFS)

initialState = [
    [" "," "," "," "," "],
    [" "," "," "," "," "],
    [" "," "," "," "," "],
    [" "," "," "," "," "],
    [" "," "," "," "," "]
]



def dfs(initialState, start, end):

    directions = [
        (1,0),
        (-1,0),
        (0,1),
        (0,-1)
    ]

    visitados = []

    recorrido = [start]

    frontier = [(start , recorrido)]

    while frontier:
        (x,y), camino = frontier.pop()

        if (x,y) == end:
            return camino
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(initialState) and 0 <= ny < len(initialState[0]):
                if (nx, ny) not in visitados:
                    visitados.append((nx,ny))
                    print(frontier)
                    frontier.append(((nx, ny), camino + [(nx,ny)]))

        

print(dfs(initialState, (0,0) , (4,4)))




