# FUZZY-PATIENTS

Queremos diseñar un sistema difuso para estimar el riesgo asociado a la fiebre de un paciente.

El sistema recibe dos entradas:

- Temperatura (°C)
- Dolor corporal (0–10)

Y produce una salida:

- Riesgo (0–10)

Se utilizará inferencias tipo Mamdani, donde:

- Las reglas son del tipo: `SI (Antecedentes) ENTONCES (Consecuente)`
- El operador AND se resuelve con mínimo.
- El operador OR se resuelve con máximo.
- La salida resultante se corta según el grado de activación de la regla (implicación).
- Las conclusiones se agregan con máximo.
- Se defuzzifica con un método intuitivo (centroide aproximado).