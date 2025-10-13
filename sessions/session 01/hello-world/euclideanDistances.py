import math
def euclidean_distance(point1, point2):
    sum = 0
    for index, p in enumerate(point1):
        sum += (p - point2[index])**2
    return round(math.sqrt(sum),2)
    
valor = euclidean_distance([2,2,2,2,2,2], [3,3,3,3,3,3])
# valor = euclidean_distance([0,0], [1,1])
# valor = euclidean_distance([0,0], [0,1])

print(valor)