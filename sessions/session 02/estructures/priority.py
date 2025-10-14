import heapq

# Crear una cola de prioridad
cola = []
heapq.heappush(cola, (2, "tarea baja prioridad"))
heapq.heappush(cola, (1, "tarea alta prioridad"))

# Extraer elementos en orden de prioridad
while cola:
    prioridad, tarea = heapq.heappop(cola)
    print(f"Ejecutando {tarea} con prioridad {prioridad}")