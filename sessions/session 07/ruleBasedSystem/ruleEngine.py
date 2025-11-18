class RuleEngine:
    def __init__(self):
        self.reglas = []

    def agregar_regla(self, condicion, accion):
        self.reglas.append((condicion, accion))

    def ejecutar(self, hechos):
        for condicion, accion in self.reglas:
            if condicion(hechos):
                accion(hechos)