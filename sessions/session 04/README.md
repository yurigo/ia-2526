# Sesión 04 — Algoritmos de juegos

Esta sesión introduce los algoritmos de búsqueda adversarial, específicamente el algoritmo Minimax, utilizado en juegos de dos jugadores con información completa.

## Contenido de la sesión

### Algoritmo Minimax

El algoritmo Minimax es fundamental en la teoría de juegos y se utiliza para tomar decisiones óptimas en juegos de suma cero entre dos jugadores (MAX y MIN).

#### Archivos incluidos

- **[minimax-pseudo.py](./minimax-pseudo.py)** - Pseudocódigo del algoritmo Minimax
  - Versión simplificada que muestra la lógica básica
  - Ilustra la recursión entre jugadores MAX y MIN
  - Incluye las funciones esenciales: terminal(), utilidad(), movimientos_posibles()

- **[minimax.py](./minimax.py)** - Implementación completa de Minimax para Tic-Tac-Toe
  - Juego completo del tres en raya (Tic-Tac-Toe)
  - Funciones de evaluación: winner(), terminal(), utility()
  - Generación de sucesores: actions(), apply()
  - Algoritmo Minimax con retorno de mejor movimiento
  - Ejemplo de uso y demostración

## Conceptos clave

### Juegos adversariales

Los juegos adversariales son entornos competitivos donde:
- Dos (o más) agentes con objetivos opuestos
- Cada jugador intenta maximizar su utilidad
- La utilidad de un jugador es inversa a la del oponente (suma cero)
- Información completa: ambos jugadores conocen el estado del juego

### Algoritmo Minimax

Minimax es un algoritmo de búsqueda que:
1. **MAX** (nosotros) busca maximizar la utilidad
2. **MIN** (oponente) busca minimizar nuestra utilidad
3. Se alterna entre niveles MAX y MIN en el árbol de búsqueda
4. Retrocede (backpropagation) los valores desde las hojas hacia la raíz

#### Pseudocódigo básico

```python
def minimax(estado, es_max):
    if terminal(estado):
        return utilidad(estado)
    
    if es_max:
        mejor_valor = -infinito
        for movimiento in movimientos_posibles(estado):
            valor = minimax(aplicar(estado, movimiento), False)
            mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else:  # es_min
        mejor_valor = +infinito
        for movimiento in movimientos_posibles(estado):
            valor = minimax(aplicar(estado, movimiento), True)
            mejor_valor = min(mejor_valor, valor)
        return mejor_valor
```

#### Función de utilidad

La función de utilidad asigna valores numéricos a estados terminales:
- **+1**: Victoria para MAX (nosotros)
- **0**: Empate
- **-1**: Victoria para MIN (oponente)

### Propiedades de Minimax

| Propiedad | Descripción |
|-----------|-------------|
| **Completitud** | ✅ Sí, si el árbol es finito |
| **Optimalidad** | ✅ Sí, contra un oponente óptimo |
| **Complejidad temporal** | O(b^m) donde b=ramificación, m=profundidad |
| **Complejidad espacial** | O(bm) para búsqueda en profundidad |

### Limitaciones y extensiones

**Limitaciones:**
- El árbol de búsqueda crece exponencialmente
- Impracticable para juegos complejos (ajedrez, go)

**Extensiones comunes:**
- **Poda Alpha-Beta**: Reduce el número de nodos evaluados sin afectar el resultado
- **Profundidad limitada**: Evalúa hasta cierta profundidad y usa función heurística
- **Minimax con tabla de transposición**: Evita recalcular posiciones ya vistas

## Ejercicios y experimentación

1. Ejecuta [minimax.py](./minimax.py) y observa cómo el algoritmo encuentra el mejor movimiento
2. Modifica el tablero inicial y verifica que el algoritmo sigue siendo óptimo
3. Implementa una versión de Minimax con límite de profundidad
4. Añade poda Alpha-Beta para mejorar la eficiencia
5. Experimenta con otros juegos simples (Conecta 4, Othello)

## Aplicaciones

- **Juegos clásicos**: Ajedrez, damas, tres en raya, go
- **Toma de decisiones**: Planificación en entornos competitivos
- **Economía y teoría de juegos**: Análisis de estrategias en mercados
- **IA en videojuegos**: NPCs que juegan de manera inteligente

---

Para conceptos relacionados con búsqueda en grafos y árboles, consulta el README de la [Sesión 02](../session%2002/README.md) y [Sesión 03](../session%2003/README.md).
