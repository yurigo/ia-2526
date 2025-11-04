from itertools import product

def symbols_in(expr):
    """Returns a set of all symbols in the logical expression."""
    if isinstance(expr, str):
        return {expr}
    op, *args = expr
    s = set()
    for a in args:
        s |= symbols_in(a)
    return s

def eval_expr(expr, model):
    """Evaluates the logical expression in the given model. """
    if isinstance(expr, str):
        return model[expr]
    op, *args = expr
    if op == "NOT": return not eval_expr(args[0], model)
    if op == "AND": return all(eval_expr(a, model) for a in args)
    if op == "OR":  return any(eval_expr(a, model) for a in args)
    if op == "IMP":
        p, q = args
        return (not eval_expr(p, model)) or eval_expr(q, model)
    if op == "IFF":
        p, q = args
        return eval_expr(p, model) == eval_expr(q, model)
    raise ValueError("Operador desconocido")

def entails(KB, query):
    """Returns True if KB entails query using truth table enumeration."""
    syms = sorted(list(symbols_in(KB) | symbols_in(query)))
    for vals in product([False, True], repeat=len(syms)):
        model = dict(zip(syms, vals))
        if eval_expr(KB, model):            # solo modelos donde KB es verdadera
            if not eval_expr(query, model): # la query debe ser verdadera ahí
                return False
    return True

def expr_to_string(expr, indent=0):
    """
    Convierte una expresión lógica (en formato de tuplas) a notación proposicional legible.
    
    Args:
        expr: Expresión lógica en formato de tuplas
        indent: Nivel de indentación (para formateo)
    
    Returns:
        String con la expresión en notación lógica
    """
    if isinstance(expr, str):
        return expr
    
    op, *args = expr
    prefix = "  " * indent
    
    if op == "NOT":
        inner = expr_to_string(args[0], indent)
        return f"¬{inner}"
    
    elif op == "AND":
        if len(args) == 1:
            return expr_to_string(args[0], indent)
        # Si hay muchos argumentos, mostrar en líneas separadas
        if len(args) > 2:
            parts = [expr_to_string(arg, indent + 1) for arg in args]
            joined = "\n" + prefix + "  ∧ ".join(parts)
            return f"({joined}\n{prefix})"
        else:
            parts = [expr_to_string(arg, indent) for arg in args]
            return f"({' ∧ '.join(parts)})"
    
    elif op == "OR":
        if len(args) == 1:
            return expr_to_string(args[0], indent)
        parts = [expr_to_string(arg, indent) for arg in args]
        return f"({' ∨ '.join(parts)})"
    
    elif op == "IMP":
        p, q = args
        antecedent = expr_to_string(p, indent)
        consequent = expr_to_string(q, indent)
        return f"({antecedent} → {consequent})"
    
    elif op == "IFF":
        p, q = args
        left = expr_to_string(p, indent)
        right = expr_to_string(q, indent)
        return f"({left} ↔ {right})"
    
    return str(expr)

def show(KB):
    """
    Muestra la base de conocimiento en notación lógica proposicional.
    
    Args:
        KB: Base de conocimiento (expresión lógica en formato de tuplas)
    """
    print("\n" + "="*70)
    print("BASE DE CONOCIMIENTO (Knowledge Base)")
    print("="*70)
    print("\nReglas en lógica proposicional:")
    print("-"*70)
    
    formula = expr_to_string(KB)
    print(formula)
    
    print("-"*70)
    print(f"Símbolos totales: {len(symbols_in(KB))}")
    print(f"Símbolos: {', '.join(sorted(symbols_in(KB)))}")
    print("="*70 + "\n")
