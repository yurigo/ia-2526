# ia-2526

Repositorio del Máster de Inteligencia Artificial y Big Data (curso 2025–2026).

## 5071. Modelos de inteligencia artificial

### Sesión 1. Introducción a la Inteligencia Artificial

#### Línea temporal esencial

- 1843: Ada Lovelace anticipa máquinas que crean patrones y música.
- 1950: Alan Turing publica “Computing Machinery and Intelligence” (Test de Turing).
- 1956: McCarthy, Minsky, Shannon y Simon acuñan “Inteligencia Artificial”.
- 1958: Frank Rosenblatt desarrolla el Perceptrón.
- 1970–1990: Inviernos de la IA por falta de resultados y recursos.
- 1997: Deep Blue (IBM) vence a Garry Kasparov.
- 2011: Siri populariza NLP en móviles.
- 2014: Google adquiere DeepMind; llegan AlphaGo y el deep learning moderno.
- 2017: “Attention Is All You Need” introduce la arquitectura Transformer.
- 2022–2025: Auge de la IA generativa (ChatGPT, DALL·E, Gemini, Claude).

#### Conceptos clave

- IA: sistemas capaces de realizar tareas que requieren inteligencia humana (razonamiento, aprendizaje, percepción).
- IA simbólica: reglas explícitas y sistemas expertos.
- IA conexionista: redes neuronales y aprendizaje a partir de datos.
- Machine Learning: aprende patrones a partir de datos.
- Deep Learning: redes profundas que capturan patrones complejos.

#### Preguntas de debate

- ¿Qué entendemos hoy por inteligencia? → Aprender, razonar, adaptarse y decidir; en humanos implica conciencia/emociones; en máquinas, inteligencia funcional sin comprensión.
- ¿Qué tiene o no tiene de “inteligente” ChatGPT? → Tiene aprendizaje de patrones, coherencia contextual y generación fluida; no tiene comprensión, conciencia, verdad ni intención.

#### Casos de uso por sector

- Salud: diagnóstico por imagen, detección de tumores.
- Educación: tutores virtuales personalizados.
- Industria: mantenimiento predictivo.
- Servicios: recomendadores (p. ej., streaming).
- Marketing: segmentación y modelos predictivos.

## 5073. Programación de inteligencia artificial

### Módulo 1 — Python (sesión 01)

Esta sección resume lo visto en clase con ejemplos prácticos y enlaces a los scripts de la carpeta `sessions/session 01/hello-world/`.

#### 1. Introducción a Python

1.1 ¿Qué es Python y por qué es tan usado en IA y Big Data?

- Sintaxis clara, gran ecosistema científico (numpy, pandas, matplotlib, scikit-learn, PyTorch, TensorFlow), comunidad activa y multiplataforma.
- Ideal para prototipado rápido, pipelines de datos y despliegues ligeros.

  1.2 Instalación y configuración del entorno (Windows)

- Requiere Python 3.x y VS Code con extensiones “Python” y “Jupyter”.
- Ver versión:

```powershell
python --version
```

> - Entorno virtual (recomendado) y Jupyter:
>
> ```powershell
> python -m venv .venv
> .\.venv\Scripts\Activate.ps1
> pip install --upgrade pip
> pip install jupyter
> ```
>
> - Ejecutar cuadernos: “Jupyter: Create New Blank Notebook” desde VS Code, o bien:
>
> ```powershell
> jupyter notebook
> ```

- Ejecutar scripts:

```powershell
python mi_script.py
```

#### 2. Fundamentos del lenguaje

2.1 Tipos de datos primitivos

```python
entero: int = 42
decimal: float = 3.14
texto: str = "Hola, IA"
booleano: bool = True
nada = None  # tipo NoneType
```

2.2 Variables y convenciones de nombres

- snake_case para variables y funciones: `mi_variable`, `calcular_media`.
- CapWords/PascalCase/UpperCamelCase para clases: `ModeloLinear`.
- Constantes en MAYÚSCULAS: `TASA_APRENDIZAJE = 0.01`. (**recuerda que no existen constantes reales en Python, es una convención**)
- Evitar nombres de una letra salvo en bucles (`i`, `j`). No empezar con dígitos.

```python
tasa_aprendizaje = 0.01
EPOCAS = 10

class ModeloLinear:
	pass
```

2.3 Comentarios (# y docstrings)

```python

# esto es un comentario

"""
 esto es un literal de cadena multilínea, si no se asigna a
 una variable, se ignora y se puede utilizar para comentarios
 multilínea y si se coloca al inicio de una función o clase,
 se usa como docstring
"""

def sumar(a: int, b: int) -> int:
	"""Suma dos enteros y devuelve el resultado.
	Args:
		a: primer sumando
		b: segundo sumando
	Returns:
		Suma de a y b
	"""
	return a + b
```

2.4 Entrada y salida (`input()`, `print()`)

```python
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}")
print("Valor:", 3, "pi≈", 3.14159, sep=" | ", end="\n")
```

Enlaces: fundamentos y control de flujo en `helloworld.py` → [sessions/session 01/hello-world/helloworld.py](sessions/session%2001/hello-world/helloworld.py)

#### 3. Operadores

3.1 Aritméticos, relacionales y lógicos

```python
a, b = 7, 3
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)  # ** potencia
print(a > b, a == b, a != b, a <= b)
print((a > 0) and (b > 0), (a < 0) or (b < 0), not (a == b))
```

3.2 Asignación y operadores abreviados

```python
x = 10
x += 5   # 15
x *= 2   # 30
x -= 1   # 29
```

3.3 Pertenencia e identidad

```python
lista = [1, 2, 3]
print(2 in lista, 4 not in lista)   # pertenencia

x = [1, 2]
y = [1, 2]
print(x == y)  # True (igualdad de valor)
print(x is y)  # False (identidad de objeto diferente)
```

Enlaces: ejemplo de calculadora y operadores → [sessions/session 01/hello-world/calculator.py](sessions/session%2001/hello-world/calculator.py), pertenencia/identidad y bucles → [helloworld.py](sessions/session%2001/hello-world/helloworld.py)

#### 4. Estructuras de control

4.1 Condicionales

```python
nota = 7.5
if nota >= 9:
	print("Sobresaliente")
elif nota >= 7:
	print("Notable")
elif nota >= 5:
	print("Aprobado")
else:
	print("Suspenso")
```

4.2 Bucles `for` y `while`

```python
for i in range(3):
	print("Iteración", i)

j = 0
while j < 3:
	print("j:", j)
	j += 1
```

4.3 Control de flujo: `break`, `continue`

```python
for n in range(10):
	if n == 5:
		break        # sale del bucle
	if n % 2 == 0:
		continue     # salta a la siguiente iteración
	print(n)
```

4.4 Bucles anidados y comprensión de listas

```python
pares = []
for i in range(3):
	for j in range(3):
		if (i + j) % 2 == 0:
			pares.append((i, j))

cuadrados = [x**2 for x in range(6)]
pares_solo = [x for x in range(10) if x % 2 == 0]
matriz = [[i*j for j in range(3)] for i in range(3)]
```

Enlace: control de flujo en `helloworld.py` → [sessions/session 01/hello-world/helloworld.py](sessions/session%2001/hello-world/helloworld.py)

#### 5. Colecciones de datos

5.1 Listas: creación, acceso, slicing, métodos

```python
nums = [10, 20, 30, 40, 50]
print(nums[0], nums[-1])        # acceso
print(nums[1:4], nums[::2])     # slicing

nums.append(60)
nums.insert(1, 15)
nums.extend([70, 80])
nums.remove(30)
ultimo = nums.pop()
nums.sort()                     # in-place
ordenada = sorted(nums, reverse=True)
print(nums, ultimo, ordenada)
```

5.2 Tuplas: inmutabilidad y desempaquetado

```python
punto = (3, 4)
# punto[0] = 10  # ❌ TypeError: tuplas son inmutables
x, y = punto
```

5.3 Conjuntos (`set`): unión, intersección, diferencia

```python
a, b = {1, 2, 3}, {3, 4, 5}
print(a | b)   # unión -> {1,2,3,4,5}
print(a & b)   # intersección -> {3}
print(a - b)   # diferencia -> {1,2}
print(a ^ b)   # diferencia simétrica -> {1,2,4,5}
```

5.4 Diccionarios (`dict`): pares clave-valor y métodos

```python
persona = {"nombre": "Ana", "edad": 30, "skills": ["python", "sql"]}
print(persona.get("edad", "desconocida"))

for k, v in persona.items():
	print(k, "->", v)

claves = list(persona.keys())
valores = list(persona.values())
persona.update({"ciudad": "Madrid"})
```

Enlace: colecciones en `colections.py` → [sessions/session 01/hello-world/colections.py](sessions/session%2001/hello-world/colections.py)

#### 6. Funciones

6.1 Definición, llamada y valores por defecto

```python
def potencia(base: float, exp: int = 2) -> float:
	return base ** exp

print(potencia(3), potencia(2, 3))
```

6.2 Parámetros posicionales y nombrados

```python
def resumen(titulo: str, autor: str, version: str = "1.0") -> None:
	print("Título:", titulo)
	print("Autor:", autor)
	print("Versión:", version)

resumen(titulo="Informe", autor="Yuri", version="1.0")
```

6.3 Retorno de valores (múltiples)

```python
def min_max(lista):
	return min(lista), max(lista)

lo, hi = min_max([3, 1, 4])
```

Enlace: funciones en `functions.py` → [sessions/session 01/hello-world/functions.py](sessions/session%2001/hello-world/functions.py)

#### 9. Manejo de errores y excepciones

9.1 `try`, `except`, `else`, `finally`

```python
def dividir(a, b):
	try:
		res = a / b
	except ZeroDivisionError:
		return "No se puede dividir por cero"
	else:
		return res
	finally:
		pass  # liberar recursos si aplica
```

Enlace: excepciones básicas → [sessions/session 01/hello-world/exceptions.py](sessions/session%2001/hello-world/exceptions.py)

#### Ejercicios prácticos de la sesión

- Distancia euclídea: [euclideanDistances.py](sessions/session%2001/hello-world/euclideanDistances.py)
- Calculadora IMC: [imcCalculator.py](sessions/session%2001/hello-world/imcCalculator.py)

---

Si detectas lagunas o quieres ampliar algún apartado (p. ej., ejemplos de código, ejercicios o rúbricas), abre un issue o propon cambios.
