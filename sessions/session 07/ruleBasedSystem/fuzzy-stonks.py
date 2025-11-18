def fuzzy_grade_down(x, left, right):
    """1 at x<=left, 0 at x>=right, linear in between."""
    if x <= left: return 1.0
    if x >= right: return 0.0
    return (right - x) / (right - left)

def fuzzy_grade_up(x, left, right):
    """0 at x<=left, 1 at x>=right, linear in between."""
    if x <= left: return 0.0
    if x >= right: return 1.0
    return (x - left) / (right - left)

def fuzzy_triangle(x, left, center, right):
    """Triangular fuzzy set."""
    if x <= left or x >= right: return 0.0
    if x == center: return 1.0
    if x < center: return (x - left) / (center - left)
    return (right - x) / (right - center)


def compute_fuzzy_sets(hechos):
    cambio = (hechos['precio'] - hechos['precio_anterior']) / hechos['precio_anterior'] * 100
    volumen_ratio = hechos['volumen'] / hechos['volumen_promedio']
    volatilidad = abs(hechos['precio'] - hechos['precio_anterior'])

    hechos['fuzzy'] = {
        # Price change fuzzy sets (%)
        'drop_small':  fuzzy_triangle(cambio, -5, -2.5, 0),
        'drop_big':    fuzzy_grade_down(cambio, -10, -3),
        'rise_small':  fuzzy_triangle(cambio, 0, 2.5, 5),
        'rise_big':    fuzzy_grade_up(cambio, 3, 10),

        # Volume fuzzy sets (relative to average)
        'vol_low':     fuzzy_grade_down(volumen_ratio, 0.3, 0.8),
        'vol_med':     fuzzy_triangle(volumen_ratio, 0.6, 1.0, 1.4),
        'vol_high':    fuzzy_grade_up(volumen_ratio, 1.1, 2.0),

        # Volatility fuzzy sets (absolute price diff)
        'quiet':       fuzzy_grade_down(volatilidad, 0, 3),
        'volatile':    fuzzy_grade_up(volatilidad, 2, 8)
    }


from ruleEngine import RuleEngine

motor = RuleEngine()

# Initialize strengths
motor.agregar_regla(
    lambda h: True,
    lambda h: h.update({'buy_strength': 0.0, 'sell_strength': 0.0})
)

# ─────────────────────────────────────────────
# BUY RULES (fuzzy)
# ─────────────────────────────────────────────

# Big drop & high volume → strong buy
motor.agregar_regla(
    lambda h: True,
    lambda h: h.update({
        'buy_strength': max(
            h['buy_strength'],
            min(h['fuzzy']['drop_big'], h['fuzzy']['vol_high'])
        )
    })
)

# Small drop & medium volume → moderate buy
motor.agregar_regla(
    lambda h: True,
    lambda h: h.update({
        'buy_strength': max(
            h['buy_strength'],
            min(h['fuzzy']['drop_small'], h['fuzzy']['vol_med'])
        )
    })
)

# Quiet + small rise = trend-follow buy
motor.agregar_regla(
    lambda h: True,
    lambda h: h.update({
        'buy_strength': max(
            h['buy_strength'],
            min(h['fuzzy']['quiet'], h['fuzzy']['rise_small'])
        )
    })
)

# ─────────────────────────────────────────────
# SELL RULES (fuzzy)
# ─────────────────────────────────────────────

motor.agregar_regla(
    lambda h: True,
    lambda h: h.update({
        'sell_strength': max(
            h['sell_strength'],
            min(h['fuzzy']['rise_big'], h['fuzzy']['vol_high'])
        )
    })
)

motor.agregar_regla(
    lambda h: True,
    lambda h: h.update({
        'sell_strength': max(
            h['sell_strength'],
            min(h['fuzzy']['drop_big'], h['fuzzy']['volatile'])
        )
    })
)

# ─────────────────────────────────────────────
# FINAL DE-FUZZIFICATION STEP
# ─────────────────────────────────────────────
def defuzzify(h):
    b, s = h['buy_strength'], h['sell_strength']
    if max(b, s) < 0.2:
        h['accion'] = 'HOLD'
    elif b > s:
        h['accion'] = 'BUY'
    else:
        h['accion'] = 'SELL'

motor.agregar_regla(
    lambda h: True,
    defuzzify
)


hechos = {
    'precio': 94,
    'precio_anterior': 100,
    'volumen': 50000,
    'volumen_promedio': 30000,
}

compute_fuzzy_sets(hechos)
motor.ejecutar(hechos)
print(hechos)
