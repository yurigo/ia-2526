import math

def opera(a, b, op):
    if (op == "s"):
        return a + b
    elif (op == "r"):
        return a - b
    elif (op == "m"):
        return a * b
    elif (op == "d"):
        try:
            return a / b
        except:
            print("Has dividido por 0. Error!")
            return None
    elif (op == "v"):
        return math.sqrt(a)
    else:
        return "No tengo ni idea de lo que me hablas"
    
a = input("Dame un numero \n")
a = int(a)
b = int(input("Dame otro \n"))
op = input("s:suma, r:resta, m:mult, d:div, v:raiz\n")

print("El resultado es: " , opera(a, b, op) )



    
