from ruleEngine import RuleEngine

motor = RuleEngine()

# ─────────────────────────────────────────────
# STEP 1 — Detect trend
# ─────────────────────────────────────────────
# If price increasing → bullish
motor.agregar_regla(
    lambda h: h['precio'] > h['precio_anterior'] * 1.02,  # +2%
    lambda h: h.update({'trend': 'bullish'})
)

# If price decreasing → bearish
motor.agregar_regla(
    lambda h: h['precio'] < h['precio_anterior'] * 0.98,  # -2%
    lambda h: h.update({'trend': 'bearish'})
)

# ─────────────────────────────────────────────
# STEP 2 — Translate trend → intent (chained)
# ─────────────────────────────────────────────
# bullish → intent: buy
motor.agregar_regla(
    lambda h: h.get('trend') == 'bullish',
    lambda h: h.update({'intent': 'buy'})
)

# bearish → intent: sell (if holding)
motor.agregar_regla(
    lambda h: h.get('trend') == 'bearish' and h.get('acciones_en_cartera', 0) > 0,
    lambda h: h.update({'intent': 'sell'})
)

# ─────────────────────────────────────────────
# STEP 3 — Apply risk filters (chaining continues)
# ─────────────────────────────────────────────
# If low volume, block buying intent
motor.agregar_regla(
    lambda h: h.get('intent') == 'buy'
              and h['volumen'] < h['volumen_promedio'] * 0.7,
    lambda h: h.update({'intent': None, 'warning': 'low_volume'})
)

# If too volatile, block selling intent
motor.agregar_regla(
    lambda h: h.get('intent') == 'sell'
              and abs(h['precio'] - h['precio_anterior']) > 10,
    lambda h: h.update({'intent': None, 'warning': 'high_volatility'})
)

# ─────────────────────────────────────────────
# STEP 4 — Intent → concrete action
# ─────────────────────────────────────────────
motor.agregar_regla(
    lambda h: h.get('intent') == 'buy',
    lambda h: h.update({'accion': 'BUY'})
)

motor.agregar_regla(
    lambda h: h.get('intent') == 'sell',
    lambda h: h.update({'accion': 'SELL'})
)

# ─────────────────────────────────────────────
# STEP 5 — Cleanup (end of chain)
# ─────────────────────────────────────────────
motor.agregar_regla(
    lambda h: 'accion' in h,
    lambda h: h.pop('intent', None)
)

hechos = {
    'precio': 104,
    'precio_anterior': 100,
    'volumen': 40000,
    'volumen_promedio': 30000,
    'acciones_en_cartera': 0
}

motor.ejecutar(hechos)
print(hechos)