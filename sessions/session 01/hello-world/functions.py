def potencia(base, exp = 2):
    """
    esta funcion hace una potencia coge la base 
    y la eleva al exponente.  si no hay valor el exponente
    es 2
    """
    return base ** exp


print(potencia(2,3))

print(potencia(2,4))
print(potencia(2,5))
print(potencia(2))
print(potencia(4))

# print(potencia.__doc__)
# help(potencia)

print(potencia(exp=4,base=9))


def min_max(lista):
    return min(lista), max(lista)


a , b = min_max([1,2,3,4,5,6,7,8,9])

print(a)
print(b)