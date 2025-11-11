# Sesión 06 — Lógica proposicional con CNF y resolución

Esta sesión se centra en la lógica proposicional utilizando la Forma Normal Conjuntiva (CNF) y el método de resolución para inferencia automática. Extiende los conceptos de la Sesión 05 con implementaciones más avanzadas.

## Contenido de la sesión

### Archivos incluidos

- **[logicCNF.py](./logicCNF.py)** - Biblioteca de lógica proposicional con CNF
  - Conversión automática a Forma Normal Conjuntiva (CNF)
  - Eliminación de implicaciones (IMP) y bicondicionales (IFF)
  - Aplicación de leyes de De Morgan
  - Distribución de OR sobre AND
  - Resolución por refutación
  - Verificación de modelos y satisfacibilidad

- **[puzzleCNF.py](./puzzleCNF.py)** - Puzzle de asignación Pokemon-Pokeballs
  - Aplicación práctica de lógica proposicional
  - Problema de asignación con restricciones
  - Generación automática de reglas
  - Uso de resolución para encontrar la solución

## Conceptos clave

### Forma Normal Conjuntiva (CNF)

La CNF es una forma estandarizada de expresar fórmulas lógicas:
- **Literal**: Una variable o su negación (P o ¬P)
- **Cláusula**: Disyunción de literales (P ∨ Q ∨ ¬R)
- **CNF**: Conjunción de cláusulas ((P ∨ Q) ∧ (¬P ∨ R) ∧ (Q ∨ ¬R))

#### Ventajas de CNF

1. **Estandarización**: Todas las fórmulas se representan uniformemente
2. **Eficiencia**: Facilita la aplicación del método de resolución
3. **Automatización**: Permite razonamiento automático mediante algoritmos

### Proceso de conversión a CNF

1. **Eliminar implicaciones**:
   - P → Q se convierte en ¬P ∨ Q
   - P ↔ Q se convierte en (¬P ∨ Q) ∧ (¬Q ∨ P)

2. **Mover negaciones hacia dentro** (Leyes de De Morgan):
   - ¬(P ∧ Q) se convierte en ¬P ∨ ¬Q
   - ¬(P ∨ Q) se convierte en ¬P ∧ ¬Q
   - ¬(¬P) se convierte en P

3. **Distribuir OR sobre AND**:
   - P ∨ (Q ∧ R) se convierte en (P ∨ Q) ∧ (P ∨ R)

### Método de resolución

La resolución es una regla de inferencia que combina dos cláusulas que contienen literales complementarios:

```
(P ∨ Q) ∧ (¬P ∨ R) ⊨ (Q ∨ R)
```

#### Resolución por refutación

Para probar que KB ⊨ α:
1. Convertir KB y ¬α a CNF
2. Añadir las cláusulas de ¬α a KB
3. Aplicar resolución repetidamente
4. Si se obtiene la cláusula vacía (contradicción) → KB ⊨ α
5. Si no se pueden generar más cláusulas → KB ⊭ α

#### Propiedades del método de resolución

| Propiedad | Descripción |
|-----------|-------------|
| **Corrección** | ✅ Si encuentra una contradicción, la conclusión es válida |
| **Completitud** | ✅ Si hay una contradicción, la encontrará |
| **Decidibilidad** | ✅ En lógica proposicional, siempre termina |

## Ejemplo: Puzzle Pokemon-Pokeballs

El archivo [puzzleCNF.py](./puzzleCNF.py) resuelve un problema de asignación:

**Problema:**
- 4 Pokemon: Pikachu, Squirtle, Bulbasaur, Charmander
- 4 Pokeballs: Pokeball, Greatball, Ultraball, Masterball
- Cada Pokemon en exactamente UNA Pokeball
- Cada Pokeball contiene exactamente UN Pokemon

**Pistas:**
- Pikachu está en Pokeball o Ultraball
- Squirtle NO está en Masterball
- Bulbasaur está en Ultraball

**Representación:**
- Símbolos: "PikachuPokeball", "SquirtleGreatball", etc.
- Reglas en CNF para cada restricción
- Resolución para encontrar la asignación única

### Estructura del código

```python
# 1. Generar símbolos
symbols = [f"{pokemon}{pokeball}" 
           for pokemon in pokemon_list 
           for pokeball in pokeball_list]

# 2. Reglas: cada Pokemon en ALGUNA Pokeball
# (PikachuPokeball ∨ PikachuGreatball ∨ PikachuUltraball ∨ PikachuMasterball)

# 3. Reglas: cada Pokemon en SOLO UNA Pokeball
# ¬(PikachuPokeball ∧ PikachuGreatball)

# 4. Pistas específicas del problema
# (PikachuPokeball ∨ PikachuUltraball)
# ¬SquirtleMasterball
# BulbasaurUltraball

# 5. Aplicar resolución para inferir la solución
```

## Diferencias con la Sesión 05

| Aspecto | Sesión 05 | Sesión 06 |
|---------|-----------|-----------|
| **Representación** | Fórmulas lógicas generales | CNF estandarizada |
| **Inferencia** | Reglas de inferencia variadas | Resolución automática |
| **Conversión** | Manual | Automática a CNF |
| **Complejidad** | Ejemplos básicos | Puzzles más complejos |

## Ejercicios y experimentación

1. Ejecuta [puzzleCNF.py](./puzzleCNF.py) y observa cómo se resuelve el puzzle
2. Modifica las pistas del puzzle y verifica que la solución cambia correctamente
3. Añade un 5º Pokemon y 5ª Pokeball, actualiza las reglas
4. Implementa tu propio puzzle de asignación (ej: personas-trabajos, estudiantes-cursos)
5. Estudia el código de [logicCNF.py](./logicCNF.py) para entender la conversión a CNF

## Aplicaciones de lógica proposicional y CNF

- **Verificación de circuitos**: Comprobar corrección de diseños hardware
- **Planificación automática**: Generar secuencias de acciones
- **Diagnóstico**: Identificar fallos en sistemas
- **SAT solvers**: Herramientas industriales para problemas combinatorios
- **Configuración de productos**: Selección de componentes compatibles
- **Puzzles lógicos**: Sudoku, Cluedo, asignaciones

## Relación con otros métodos

- **CNF + Resolución**: Método general pero puede ser lento
- **Tablas de verdad**: Exhaustivo pero inviable para muchas variables
- **Encadenamiento hacia adelante/atrás**: Más eficiente para problemas específicos
- **SAT moderno**: Usa CNF con optimizaciones avanzadas (DPLL, CDCL)

---

Para conceptos básicos de lógica proposicional y reglas de inferencia, consulta el README de la [Sesión 05](../session%2005/README.md).
