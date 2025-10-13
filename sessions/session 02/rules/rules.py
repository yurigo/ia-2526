class MotorDeReglas:
    def __init__(self):
        self.reglas = []

    def agregar_regla(self, condicion, accion):
        self.reglas.append((condicion, accion))

    def ejecutar(self, hechos):
        for condicion, accion in self.reglas:
            if condicion(hechos):
                accion(hechos)


motor = MotorDeReglas()

motor.agregar_regla(
    lambda hechos: hechos.get('lluvia', False),
    lambda hechos: hechos.update({'llevar_paraguas': True})
)

motor.agregar_regla(
    lambda hechos: not hechos.get('lluvia', False),
    lambda hechos: hechos.update({'llevar_paraguas': False})
)

motor.agregar_regla(
    lambda hechos: hechos.get('llevar_paraguas', False),
    lambda hechos: hechos.update({'llevar_chubasquero': True})
)

motor.agregar_regla(
    lambda hechos: hechos.get('llevar_chubasquero', False),
    # borrar la entrada 'llevar_paraguas' si existe
    lambda hechos: hechos.pop('llevar_paraguas', None)
)

hechos = {'lluvia': True}
motor.ejecutar(hechos)

print(hechos)  # {'lluvia': True, 'llevar_paraguas': True}