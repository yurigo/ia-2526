from ruleEngine import RuleEngine

motor = RuleEngine()

# ─────────────────────────────────────────────
# BUY RULES
# ─────────────────────────────────────────────

# Buy if price dropped more than 3%
motor.agregar_regla(
    lambda h: h['precio'] < h['precio_anterior'] * 0.97,
    lambda h: h.update({'buy_signal': True})
)

# Do NOT buy if volume is significantly lower than average
motor.agregar_regla(
    lambda h: h.get('buy_signal', False) and h['volumen'] < h['volumen_promedio'] * 0.7,
    lambda h: h.update({'buy_signal': False, 'low_volume_warning': True})
)

# If buy_signal and no stock held → generate real buy action
motor.agregar_regla(
    lambda h: h.get('buy_signal', False) and h.get('acciones_en_cartera', 0) == 0,
    lambda h: h.update({'accion': 'BUY'})
)

# ─────────────────────────────────────────────
# SELL RULES
# ─────────────────────────────────────────────

# Sell if price increased more than 5%
motor.agregar_regla(
    lambda h: h['precio'] > h['precio_anterior'] * 1.05 
               and h.get('acciones_en_cartera', 0) > 0,
    lambda h: h.update({'accion': 'SELL'})
)

# Stop-loss (sell if price falls more than 8%)
motor.agregar_regla(
    lambda h: h['precio'] < h['precio_anterior'] * 0.92
               and h.get('acciones_en_cartera', 0) > 0,
    lambda h: h.update({'accion': 'SELL_STOPLOSS'})
)

# ─────────────────────────────────────────────
# CLEANUP RULES
# ─────────────────────────────────────────────

# If we decide to sell or buy, remove warnings
motor.agregar_regla(
    lambda h: h.get('accion') in ('BUY', 'SELL', 'SELL_STOPLOSS'),
    lambda h: h.pop('low_volume_warning', None)
)


# hechos = {
#     'precio': 100,
#     'precio_anterior': 15,
#     'volumen': 20000,
#     'volumen_promedio': 30000,
#     'acciones_en_cartera': 0
# }


hechos = {
    'precio': 120,
    'precio_anterior': 100,
    'volumen': 30001,
    'volumen_promedio': 30000,
    'acciones_en_cartera': 20
}

motor.ejecutar(hechos)

print(hechos)