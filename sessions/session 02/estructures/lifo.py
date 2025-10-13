# lifo
# last in, first out

# pila (stack)
pila = []

# añadir elementos
pila.append("tarea 1")
pila.append("tarea 2")
pila.append("tarea 3")
print(pila)  # ['tarea 1', 'tarea 2', 'tarea 3']

# extraer elementos
while pila:
    tarea = pila.pop()
    print(f"Ejecutando {tarea}")