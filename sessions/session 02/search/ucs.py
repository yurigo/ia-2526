# Depth-first search (DFS)
import heapq

initialState = [
    [0,4,0,0,4],
    [0,0,0,0,4],
    [0,0,4,0,4],
    [0,0,0,0,0],
    [0,0,0,4,0]
]


def ucs(initialState, start, end):

    directions = [
        (1,0),
        (-1,0),
        (0,1),
        (0,-1)
    ]

    visitados = []

    recorrido = [start]

    frontier = []
    heapq.heappush( frontier, ( 0 , (start, recorrido)))

    while frontier:
        
        priority , ((x,y), camino) = heapq.heappop(frontier) #frontier.pop()
        print(priority)

        if (x,y) == end:
            return camino
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(initialState) and 0 <= ny < len(initialState[0]):
                if (nx, ny) not in visitados:
                    visitados.append((nx,ny))
                    print(frontier)
                    # frontier.append(((nx, ny), camino + [(nx,ny)]))

                    coste_de_estar_aqui = 0
                    for x,y in camino:
                        coste_de_estar_aqui += initialState[x][y]
                    coste_de_estar_aqui += initialState[nx][ny]
                    

                    heapq.heappush(frontier, ( coste_de_estar_aqui , (((nx, ny), camino + [(nx,ny)]))) )

        

print(ucs(initialState, (0,0) , (4,4)))




