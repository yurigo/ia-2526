# calcula el índice de masa corporal. pide al 
# usuario lo que necesites para calcular

"""
segun el imc mostrar el mensaje:

IMC	Clasificación
18,5	Peso insuficiente
18,5-24,9	Normopeso
25-26,9	Sobrepeso grado I
27-29,9	Sobrepeso grado II (preobesidad)
30-34,9	Obesidad de tipo I
35-39,9	Obesidad de tipo II
40-49,9	Obesidad de tipo III (mórbida)
≥50	Obesidad de tipo IV (extrema)
"""

def calculaIMC(peso, altura):
    return peso / (altura * altura)

def getMensaje(imc):
    if (imc < 18.5):
        return "Peso insuficiente"
    elif (imc < 24.9):
        return "Normopeso"
    elif (imc < 26.9):
        return "Sobrepeso grado I"
    elif (imc < 29.9):
        return "Sobrepeso grado II (preobesidad)"
    elif (imc < 34.9):
        return "Obesidad de tipo I (extrema)"
    elif (imc < 39,9):
        return "Obesidad de tipo II (extrema)"
    elif (imc < 49,9):
        return "Obesidad de tipo III (mórbida)"
    else:
        return "Obesidad de tipo IV (extrema)"


peso = float(input("Peso(kg)"))
altura = float(input("altura(m)"))

print("tu IMC es:" , calculaIMC(peso, altura))
print("estas en:" , getMensaje(calculaIMC(peso, altura)))

