# fifo
# first in, first out

# cola (queue)

cola = []

# añadir elementos
cola.append("tarea 1")
cola.append("tarea 2")
cola.append("tarea 3")
print(cola)  # ['tarea 1', 'tarea 2', 'tarea 3']

# extraer elementos
while cola:
    tarea = cola.pop(0)
    print(f"Ejecutando {tarea}")