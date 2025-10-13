class MotorDeReglas:
    def __init__(self):
        self.reglas = []

    def agregar_regla(self, condicion, accion):
        self.reglas.append((condicion, accion))

    def ejecutar(self, hechos):
        for condicion, accion in self.reglas:
            if condicion(hechos):
                accion(hechos)


# Ejemplo sencillo y distinto: planificador de estudio
# - Sugiere bebida, técnica, prioridades y equipamiento según los hechos.

motor = MotorDeReglas()

# 0) Valor por defecto para bebida si no se especifica
motor.agregar_regla(
    lambda h: 'bebida' not in h,
    lambda h: h.update({'bebida': 'agua'})
)

# 1) Bebida en función del sueño y disponibilidad
motor.agregar_regla(
    lambda h: h.get('sueno', False) and h.get('cafe_disponible', False),
    lambda h: h.update({'bebida': 'cafe'})
)

motor.agregar_regla(
    lambda h: h.get('sueno', False) and not h.get('cafe_disponible', False) and 'bebida' not in h,
    lambda h: h.update({'bebida': 'te'})
)

# 2) Si es tarde, evitar cafeína fuerte
motor.agregar_regla(
    lambda h: h.get('hora', 0) >= 18 and h.get('bebida') == 'cafe',
    lambda h: h.update({'bebida': 'descafeinado'})
)

# 3) Entorno: si hay ruido, usar auriculares y música suave
motor.agregar_regla(
    lambda h: h.get('ruido') == 'alto',
    lambda h: h.update({'usar_auriculares': True})
)

motor.agregar_regla(
    lambda h: h.get('usar_auriculares', False),
    lambda h: h.update({'musica': 'lofi'})
)

# 4) Técnica de estudio según duración
motor.agregar_regla(
    lambda h: h.get('duracion_min', 0) >= 50,
    lambda h: h.update({'tecnica': 'pomodoro', 'min_descanso': 5})
)

# 5) Prioridad según examen
motor.agregar_regla(
    lambda h: h.get('examen_manana', False),
    lambda h: h.update({'prioridad': 'repaso'})
)

motor.agregar_regla(
    lambda h: not h.get('examen_manana', False) and 'prioridad' not in h,
    lambda h: h.update({'prioridad': 'proyecto'})
)

# 6) Snack si hay hambre
motor.agregar_regla(
    lambda h: h.get('hambre', False),
    lambda h: h.update({'snack': 'fruta'})
)

# 7) Mensaje de recomendación simple al final
motor.agregar_regla(
    lambda h: 'recomendacion' not in h and 'prioridad' in h and 'bebida' in h,
    lambda h: h.update({'recomendacion': f"Prioriza {h['prioridad']}. Bebe {h['bebida']}."})
)


# 4 escenarios de demostración
escenarios = [
    (
        'S1) Noche con sueño, café y ruido alto',
        {
            'hora': 20,
            'duracion_min': 90,
            'sueno': True,
            'cafe_disponible': True,
            'ruido': 'alto',
            'examen_manana': True,
            'hambre': True,
        },
    ),
    (
        'S2) Mañana tranquila, sin sueño ni hambre',
        {
            'hora': 10,
            'duracion_min': 40,
            'sueno': False,
            'cafe_disponible': False,
            'ruido': 'bajo',
            'examen_manana': False,
            'hambre': False,
        },
    ),
    (
        'S3) Tarde con sueño pero sin café',
        {
            'hora': 17,
            'duracion_min': 120,
            'sueno': True,
            'cafe_disponible': False,
            'ruido': 'alto',
            'examen_manana': False,
            'hambre': True,
        },
    ),
    (
        'S4) Media tarde sin sueño, con examen mañana',
        {
            'hora': 16,
            'duracion_min': 60,
            'sueno': False,
            'cafe_disponible': True,
            'ruido': 'alto',
            'examen_manana': True,
            'hambre': False,
        },
    ),
]

for titulo, hechos in escenarios:
    print(f"\n=== {titulo} ===")
    motor.ejecutar(hechos)
    for k in sorted(hechos.keys()):
        print(f"{k}: {hechos[k]}")
