import os

os.system('cls')

# print("Hola!")

# # comentario
# """
# esto de aqui es un string
# multilinea
# """

# # tipos

# entero = 1356345726458723645872364867
# decimal = 13.89
# str = "Hola que tal"
# bool = True
# nada = None

# hola_que_tal = "lelele"
# CONSTANTES = 40
# CONSTANTES = 60

# # class UpperCamelCase

# print(CONSTANTES)

# print("Escribeme algo")
# algo = input("Escribeme algo \n")

# print(algo)

# a = 3 * 2
# b = a - 8
# c = b / 2
# d = c - 1
# e = d % 2
# f = e ** 4
# print (a,b,c,d)

# x = 0
# x = x + 1
# x += 1
# x -= 1
# x *= 2
# x /= 3

# Pertenencia e identidad

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("el 20 esta?" , 20 in lista)
print("el 2?" , 2 in lista)

x = [1,2]
y = [1,2]

print(x == y)
print(x is y)


if ( True ):
    print("Esto se ejecuta")
elif ( False ):
    print("Esto no se ejecuta nunca")
else:
    print("Esto no")

# Bucles

for value in [5,5,5,4,5]:
    print("Iteración: " , value)


for index , value in enumerate([5,5,5,4,5]):
    print("Iteración: " , index, " -> ", value)


contador = 0

while (contador < 10):
    contador += 1
    if (contador == 2): 
        continue
    if (contador == 5):
        print("El contador es 5")
        break
    print("voy por el: " , contador)
else:
    print("he llegado al final sin encontrar el resultado")


print("he salido del while")



    


