# Conceptos

- Agentes, estados, acciones, costes y objetivo.
  - Define formalmente qué es un problema de búsqueda y qué es un agente racional.
  - Usa ejemplos simples (laberinto, robot, puzzle 8).
  - Introduce la idea de función de coste y criterio de optimalidad.
- Búsqueda no informada: BFS, DFS, UCS.
- Búsqueda informada: heurísticas admisibles, A\*.
- Sistemas basados en reglas: reglas de producción, encadenamiento hacia delante.
- Ética y seguridad by design: impacto de métricas y fairness en asignación de recursos

## Agentes

Un agente es cualquier entidad que percibe su entorno y actúa sobre él para alcanzar un objetivo.

Clasificación de agentes?

Por ejemplo, un agente puede ser:

- Un robot que decide hacia dónde moverse.
- Un programa que resuelve un puzzle.
- Un sistema de recomendación que elige qué contenido mostrar.

> Un agente racional es aquel que toma decisiones óptimas basadas en la información disponible para maximizar su rendimiento.

## Pseudo-código

```
función AGENTE(ENTORNO) {
  estado ← ENTORNO.OBTENER_ESTADO()
  acción ← PLANIFICAR(estado)
  ENTORNO.EJECUTAR(acción)
}
```

## Problemas de búsqueda

Un problema de búsqueda describe una tarea que el agente debe resolver moviéndose entre estados posibles hasta alcanzar uno que cumpla el objetivo.

Un problema de búsqueda se define por:

- Un conjunto de estados posibles.
- Un estado inicial.
- Un conjunto de acciones que permiten moverse entre estados.
- Una función de transición que define el resultado de aplicar una acción en un estado.
- Un conjunto de estados objetivo.
- Una función de coste que asigna un coste a cada acción.

El objetivo es encontrar una secuencia de acciones (un camino) desde el estado inicial hasta un estado objetivo que minimice el coste total.

### Ejemplo robot:

| Elemento                 | Significado                       | Ejemplo (laberinto)                   |
| ------------------------ | --------------------------------- | ------------------------------------- |
| **Estado inicial**       | Punto de partida                  | Casilla donde empieza el robot        |
| **Acciones**             | Movimientos posibles              | ↑ ↓ ← →                               |
| **Modelo de transición** | Qué pasa si aplico una acción     | Mover ↑ desde (2,3) → (2,2)           |
| **Estado objetivo**      | Condición de éxito                | Llegar a la salida                    |
| **Coste de camino**      | Suma de los costes de cada acción | 1 por paso, o mayor si hay obstáculos |

### Busqueda no informada

| Algoritmo                | Estructura                              | Completitud                          | Optimalidad                  | Complejidad (en nodos)               |
| ------------------------ | --------------------------------------- | ------------------------------------ | ---------------------------- | ------------------------------------ |
| **BFS** (anchura)        | FIFO                                    | ✅ siempre encuentra si hay solución | ✅ si los costes son iguales | Exponencial en profundidad           |
| **DFS** (profundidad)    | LIFO                                    | ❌ puede perderse en ramas infinitas | ❌ no garantiza mejor coste  | Menor memoria, pero riesgo de bucles |
| **UCS** (coste uniforme) | Cola de prioridad (por coste acumulado) | ✅                                   | ✅ (si costes positivos)     | Similar a BFS, pero ordena por coste |

> UCS ≈ “BFS ponderado”:
> si todos los costes = 1 → se comporta como BFS.
> Si hay caminos más caros, UCS elige el de menor coste total g(n).

#### Pseudo-código BFS

```
BFS(problem):
  frontera ← cola([estado_inicial])
  visitados ← {}
  mientras frontera no vacía:
    n ← extraer_primero(frontera)
    si objetivo(n): devolver ruta(n)
    para cada a en acciones(n):
      s' ← aplicar(n, a)
      si s' ∉ visitados:
        marcar visitados
        añadir s' a frontera
```

#### Pseudo-código DFS

```
DFS(problem):
  frontera ← pila([estado_inicial])
  visitados ← {}
  mientras frontera no vacía:
    n ← extraer_ultimo(frontera)
    si objetivo(n): devolver ruta(n)
    para cada a en acciones(n):
      s' ← aplicar(n, a)
      si s' ∉ visitados:
        marcar visitados
        añadir s' a frontera
```

#### Pseudo-código UCS

```
UCS(problem):
  frontera ← heap([(0, estado_inicial)])  # (coste, estado)
  g[estado_inicial] ← 0
  mientras frontera no vacía:
    (c, n) ← pop_heap(frontera)
    si objetivo(n): devolver ruta(n)
    para cada (a, coste, s') en sucesores(n):
      tentativo ← g[n] + coste
      si s' no visto o tentativo < g[s']:
        g[s'] ← tentativo
        push_heap(frontera, (tentativo, s'))
```

> Además de las búsquedas clásicas (BFS, DFS, UCS), existe una técnica de exploración muy usada en problemas combinatorios: el Backtracking, que combina el recorrido en profundidad con poda de soluciones inválidas.

### Backtracking (vuelta atrás)

El Backtracking es una técnica de búsqueda sistemática que explora soluciones parciales y retrocede cuando una decisión no puede conducir a una solución válida.

#### Diferencias con DFS

- DFS recorre todo el árbol sin considerar si un camino es válido hasta llegar al final.
- Backtracking "razona" durante la exploración: **descarta ramas** tan pronto como detecta una contradicción.

#### Ejemplos de uso

- Sudoku, 8 reinas, combinaciones, puzzles, planificación con restricciones.

#### Pseudocódigo

```
backtrack(solución):
  si solución completa:
    mostrar(solución)
  si no:
    para cada opción válida:
      añadir opción
      si cumple restricciones:
        backtrack(solución)
      eliminar opción  # ← vuelta atrás (retroceso)
```

### Búsqueda informada

El agente usa conocimiento adicional (heurísticas) para guiar la búsqueda.

#### Heurística

Una heurística h(n) es una función que estima el coste desde el estado n hasta el objetivo.

> Es una estimación del coste restante hasta el objetivo.
> No es el coste real, sino una aproximación que ayuda a priorizar estados.
> Ejemplo: distancia a vuelo de pajaro en un mapa (Manhattan o euclídea).

#### Heurísticas admisibles

Una heurística h(n) es admisible si nunca sobreestima el coste real desde n hasta el objetivo.

¿Qué importancia tiene que una heurística sea admisible?

- Garantiza que algoritmos como A\* encontrarán la solución óptima.
- Si h(n) es admisible, A\* es completo y óptimo.
- Ejemplo: en un mapa, la distancia en línea recta es admisible si el coste real es la distancia por carretera (nunca será mayor).

#### Algoritmos informados

| Algoritmo  | Estructura                             | Completitud | Optimalidad            | Complejidad (en nodos)        |
| ---------- | -------------------------------------- | ----------- | ---------------------- | ----------------------------- |
| **A\***    | Cola de prioridad (f(n) = g(n) + h(n)) | ✅          | ✅ (si h es admisible) | Depende de la calidad de h(n) |
| **Greedy** | Cola de prioridad (h(n))               | ❌          | ❌                     | Puede ser muy ineficiente     |

##### A\*

Combina coste real g(n) y heurística h(n):
f(n) = g(n) + h(n)

- g(n): coste desde el inicio hasta n.
- h(n): estimación del coste desde n hasta el objetivo.
- f(n): coste total estimado pasando por n.

El algoritmo expande primero el nodo menor f(n). De este modo prioriza caminos prometedores y evita explorar tanto como bfs o ucs.

##### Pseudo-código A\*

```
A*(problem, h):
  frontera ← heap([(f(ini), ini)])
  g[ini] ← 0
  mientras frontera no vacía:
    (f, n) ← pop_heap(frontera)
    si objetivo(n): devolver ruta(n)
    para cada (a, c, s') en sucesores(n):
      tentativo ← g[n] + c
      si s' no visto o tentativo < g[s']:
        g[s'] ← tentativo
        f' ← g[s'] + h(s')
        push_heap(frontera, (f', s'))
```

##### Greedy

Deja de lado el coste real g(n) y solo usa la heurística h(n) para decidir qué nodo expandir primero.

Greedy(n) = h(n)

##### Pseudo-código Greedy

```
Greedy(problem, h):
  frontera ← heap([(h(ini), ini)])
  mientras frontera no vacía:
    (h, n) ← pop_heap(frontera)
    si objetivo(n): devolver ruta(n)
    para cada (a, c, s') en sucesores(n):
      si s' no visto:
        push_heap(frontera, (h(s'), s'))
```

#### Micro-motor de reglas

Un sistema basado en reglas utiliza un conjunto de reglas de producción para tomar decisiones o inferir nuevos hechos a partir de un conjunto inicial de hechos.

##### Ejemplo simple de motor de reglas

```pseudo
MotorDeReglas:
  reglas ← []

  agregar_regla(condición, acción):
    reglas.append((condición, acción))

  ejecutar(hechos):
    para cada (condición, acción) en reglas:
      si condición(hechos):
        acción(hechos)
```

# Programación de IA

Estructuras y patrones mínimos para IA clásica: grafos, colas de prioridad, búsqueda (BFS, UCS, A\*) y un micro–motor de reglas. Alineado con 5073: caracterizar lenguajes y desarrollar una aplicación de IA en entorno de modelado ligero (listas/dict, heapq) y evaluación de resultados.

## grafos

Un grafo es una estructura que representa relaciones entre objetos. Está compuesto por:

- Nodos (o vértices): representan los objetos.
- Aristas (o arcos): representan las relaciones entre los nodos. Pueden ser dirigidas o no dirigidas, y pueden tener pesos (costes).
  Los grafos se utilizan en IA para modelar problemas como redes de transporte, mapas, redes sociales y más.

```python
# Representación de un grafo usando un diccionario de listas de adyacencia
grafo = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}
```

```python
# Ejemplo de uso de un grafo para representar un mapa
class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregar_arista(self, origen, destino, peso=1):
        if origen not in self.adyacencia:
            self.adyacencia[origen] = []
        self.adyacencia[origen].append((destino, peso))

    def obtener_sucesores(self, nodo):
        return self.adyacencia.get(nodo, [])

g = Grafo()
g.agregar_arista('A', 'B', 1)
g.agregar_arista('A', 'C', 4)
g.agregar_arista('B', 'C', 2)
g.agregar_arista('B', 'D', 5)
g.agregar_arista('C', 'D', 1)
print(g.obtener_sucesores('A'))  # [('B', 1), ('C', 4)]
```

## Colas de prioridad

Una cola de prioridad es una estructura de datos que permite almacenar elementos con una prioridad asociada. Los elementos con mayor prioridad se extraen antes que los de menor prioridad. En Python, se puede implementar usando el módulo `heapq`.

```python
import heapq

# Crear una cola de prioridad
cola = []
heapq.heappush(cola, (2, "tarea baja prioridad"))
heapq.heappush(cola, (1, "tarea alta prioridad"))

# Extraer elementos en orden de prioridad
while cola:
    prioridad, tarea = heapq.heappop(cola)
    print(f"Ejecutando {tarea} con prioridad {prioridad}")
```

## Búsqueda (BFS, DFS UCS, A\*)

Implementación de los algoritmos de búsqueda:

### DFS

```python
def dfs(grafo, inicio, objetivo, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(inicio)
    if inicio == objetivo:
        return True
    for vecino, _ in grafo.obtener_sucesores(inicio):
        if vecino not in visitados:
            if dfs(grafo, vecino, objetivo, visitados):
                return True
    return False
```

### BFS

```python
def bfs(grafo, inicio, objetivo):
    visitados = set()
    cola = deque([inicio])
    while cola:
        nodo = cola.popleft()
        if nodo == objetivo:
            return True
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino, _ in grafo.obtener_sucesores(nodo):
                if vecino not in visitados:
                    cola.append(vecino)
    return False
```

### UCS

```python
def ucs(grafo, inicio, objetivo):
    visitados = set()
    cola = [(0, inicio)]
    while cola:
        costo, nodo = heapq.heappop(cola)
        if nodo == objetivo:
            return True
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino, peso in grafo.obtener_sucesores(nodo):
                if vecino not in visitados:
                    heapq.heappush(cola, (costo + peso, vecino))
    return False
```

```python
def a_star(grafo, inicio, objetivo, heuristica):
    visitados = set()
    cola = [(heuristica(inicio), inicio)]
    while cola:
        f, nodo = heapq.heappop(cola)
        if nodo == objetivo:
            return True
        if nodo not in visitados:
            visitados.add(nodo)
            for vecino, peso in grafo.obtener_sucesores(nodo):
                if vecino not in visitados:
                    g = heuristica(nodo) + peso
                    heapq.heappush(cola, (g, vecino))
    return False
```

### Motor de reglas simple

```python
class MotorDeReglas:
    def __init__(self):
        self.reglas = []

    def agregar_regla(self, condicion, accion):
        self.reglas.append((condicion, accion))

    def ejecutar(self, hechos):
        for condicion, accion in self.reglas:
            if condicion(hechos):
                accion(hechos)

# Ejemplo de uso
motor = MotorDeReglas()
motor.agregar_regla(
    lambda hechos: hechos.get('lluvia', False),
    lambda hechos: hechos.update({'llevar_paraguas': True})
)
hechos = {'lluvia': True}
motor.ejecutar(hechos)
print(hechos)  # {'lluvia': True, 'llevar_paraguas': True}
```
