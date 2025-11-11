# Sesión 03 — Algoritmos de búsqueda avanzados

Esta sesión profundiza en los algoritmos de búsqueda, tanto no informados como informados, con implementaciones prácticas que incluyen gestión de costes, reconstrucción de caminos y comparaciones de rendimiento.

## Contenido de la sesión

### Implementaciones básicas ([search/](./search/))

Conjunto de implementaciones básicas de algoritmos de búsqueda que ilustran los conceptos fundamentales:

- **BFS (Breadth-First Search)** - [bfs.py](./search/bfs.py)
  - Búsqueda en anchura sin considerar costes
  - Explora todos los nodos nivel por nivel
  - Garantiza encontrar la solución más corta en número de pasos

- **BFS con costes** - [bfs-with-cost.py](./search/bfs-with-cost.py)
  - Variante de BFS que considera los costes de las transiciones
  - Mantiene la estructura FIFO pero registra costes acumulados

- **DFS (Depth-First Search)** - [dfs.py](./search/dfs.py)
  - Búsqueda en profundidad
  - Explora una rama completa antes de retroceder
  - Usa menos memoria que BFS pero no garantiza optimalidad

- **DFS con costes** - [dfs-with-costs.py](./search/dfs-with-costs.py)
  - Variante de DFS que registra costes de los caminos explorados

- **UCS (Uniform Cost Search)** - [ucs.py](./search/ucs.py)
  - Búsqueda de coste uniforme
  - Expande primero los nodos con menor coste acumulado
  - Garantiza encontrar la solución de menor coste

- **UCS con costes** - [ucs-with-costs.py](./search/ucs-with-costs.py)
  - Implementación detallada de UCS con seguimiento de costes

- **A\* (A-Star)** - [a-star.py](./search/a-star.py)
  - Búsqueda informada que usa heurística
  - Combina coste real g(n) y estimación heurística h(n)
  - f(n) = g(n) + h(n)
  - Es óptimo si la heurística es admisible

- **Comparación** - [comparison.py](./search/comparison.py)
  - Script que compara el rendimiento de diferentes algoritmos
  - Mide nodos explorados y tiempo de ejecución
  - Útil para entender trade-offs entre algoritmos

### Implementaciones mejoradas ([improved/](./improved/))

Versiones optimizadas de los algoritmos principales con mejor gestión de caminos y estados:

- **BFS mejorado** - [bfs.py](./improved/bfs.py)
  - Reconstrucción completa de caminos
  - Manejo robusto de estados visitados
  - Optimizaciones de memoria

- **DFS mejorado** - [dfs.py](./improved/dfs.py)
  - Implementación iterativa más eficiente
  - Control de profundidad máxima
  - Mejor manejo de ciclos

- **UCS mejorado** - [ucs.py](./improved/ucs.py)
  - Uso de heap (cola de prioridad) optimizado
  - Actualización eficiente de costes
  - Reconstrucción de camino óptimo

- **A\* mejorado** - [astar.py](./improved/astar.py)
  - Implementación completa con heurísticas
  - Gestión eficiente de la frontera
  - Detección de caminos redundantes

## Conceptos clave

### Búsqueda no informada

Los algoritmos de búsqueda no informada no tienen información sobre qué tan cerca está un estado del objetivo. Solo conocen:
- El estado inicial
- Las acciones posibles
- El test de objetivo
- El coste de cada paso (en algunos casos)

### Búsqueda informada

Los algoritmos de búsqueda informada usan conocimiento adicional sobre el problema en forma de **heurísticas**:

- **Heurística h(n)**: Estimación del coste desde el nodo n hasta el objetivo
- **Admisibilidad**: Una heurística es admisible si nunca sobreestima el coste real
- **Consistencia**: h(n) ≤ coste(n, a, n') + h(n') para todo sucesor n' de n

### Comparación de algoritmos

| Algoritmo | Completo | Óptimo | Complejidad temporal | Complejidad espacial |
|-----------|----------|--------|---------------------|---------------------|
| BFS | ✅ | ✅ (coste uniforme) | O(b^d) | O(b^d) |
| DFS | ❌ | ❌ | O(b^m) | O(bm) |
| UCS | ✅ | ✅ | O(b^(C*/ε)) | O(b^(C*/ε)) |
| A\* | ✅ | ✅ (h admisible) | O(b^d) | O(b^d) |

Donde:
- b = factor de ramificación
- d = profundidad de la solución
- m = profundidad máxima del árbol
- C* = coste de la solución óptima
- ε = menor coste de paso

## Ejercicios y experimentación

1. Ejecuta [comparison.py](./search/comparison.py) para ver las diferencias de rendimiento
2. Modifica las heurísticas en A\* para ver cómo afecta al rendimiento
3. Compara las implementaciones básicas con las mejoradas
4. Experimenta con diferentes tipos de laberintos y grafos

---

Para más detalles sobre búsqueda en IA, consulta el README de la [Sesión 02](../session%2002/README.md) que introduce los conceptos fundamentales.
