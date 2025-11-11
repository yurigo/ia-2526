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

def to_cnf(expr):
    """Converts a logical expression to Conjunctive Normal Form (CNF)."""
    # Eliminar IMP y IFF
    expr = eliminate_implications(expr)
    # Mover NOT hacia adentro (Ley de De Morgan)
    expr = move_not_inwards(expr)
    # Distribuir OR sobre AND
    expr = distribute_or_over_and(expr)
    return expr

def eliminate_implications(expr):
    """Elimina implicaciones (IMP) y bicondicionales (IFF)."""
    if isinstance(expr, str):
        return expr
    
    op, *args = expr
    args = [eliminate_implications(arg) for arg in args]
    
    if op == "IMP":
        # P → Q se convierte en ¬P ∨ Q
        p, q = args
        return ("OR", ("NOT", p), q)
    elif op == "IFF":
        # P ↔ Q se convierte en (P → Q) ∧ (Q → P)
        # que es (¬P ∨ Q) ∧ (¬Q ∨ P)
        p, q = args
        return ("AND", 
                ("OR", ("NOT", p), q),
                ("OR", ("NOT", q), p))
    else:
        return (op, *args)

def move_not_inwards(expr):
    """Aplica las leyes de De Morgan para mover NOT hacia adentro."""
    if isinstance(expr, str):
        return expr
    
    op, *args = expr
    
    if op == "NOT":
        inner = args[0]
        if isinstance(inner, str):
            return expr
        
        inner_op, *inner_args = inner
        
        if inner_op == "NOT":
            # ¬¬P = P
            return move_not_inwards(inner_args[0])
        elif inner_op == "AND":
            # ¬(P ∧ Q) = ¬P ∨ ¬Q
            return move_not_inwards(("OR", *[("NOT", arg) for arg in inner_args]))
        elif inner_op == "OR":
            # ¬(P ∨ Q) = ¬P ∧ ¬Q
            return move_not_inwards(("AND", *[("NOT", arg) for arg in inner_args]))
        else:
            return ("NOT", move_not_inwards(inner))
    else:
        return (op, *[move_not_inwards(arg) for arg in args])

def distribute_or_over_and(expr):
    """Distribuye OR sobre AND: (P ∨ (Q ∧ R)) = (P ∨ Q) ∧ (P ∨ R)."""
    if isinstance(expr, str):
        return expr
    
    op, *args = expr
    args = [distribute_or_over_and(arg) for arg in args]
    
    if op == "OR":
        # Buscar si algún argumento es un AND
        and_args = [arg for arg in args if isinstance(arg, tuple) and arg[0] == "AND"]
        other_args = [arg for arg in args if arg not in and_args]
        
        if and_args:
            # Tomar el primer AND y distribuir
            and_expr = and_args[0]
            _, *and_clauses = and_expr
            rest = other_args + and_args[1:]
            
            # (A ∨ B ∨ (C ∧ D)) = (A ∨ B ∨ C) ∧ (A ∨ B ∨ D)
            distributed = ("AND", *[
                distribute_or_over_and(("OR", *rest, clause))
                for clause in and_clauses
            ])
            return distributed
        else:
            return ("OR", *args)
    elif op == "AND":
        return ("AND", *args)
    else:
        return (op, *args)

def eval_expr(expr, model):
    """Evaluates the logical expression in the given model."""
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

def to_clauses(cnf_expr):
    """Convierte una expresión CNF a un conjunto de cláusulas (conjuntos de literales)."""
    
    def extract_clauses(expr):
        if isinstance(expr, str):
            # Un literal solo
            return [frozenset([expr])]
        
        op, *args = expr
        
        if op == "AND":
            # Concatenar todas las cláusulas de cada argumento
            result = []
            for arg in args:
                result.extend(extract_clauses(arg))
            return result
        elif op == "OR":
            # Una cláusula con múltiples literales
            literals = []
            for arg in args:
                if isinstance(arg, str):
                    literals.append(arg)
                elif isinstance(arg, tuple) and arg[0] == "NOT":
                    literals.append(arg)
                else:
                    # Si hay un OR anidado, aplanar recursivamente
                    sub_clauses = extract_clauses(arg)
                    # Para OR, queremos unir los literales
                    for clause in sub_clauses:
                        literals.extend(list(clause))
            return [frozenset(literals)]
        elif op == "NOT":
            return [frozenset([expr])]
        else:
            return [frozenset()]
    
    return extract_clauses(cnf_expr)

def negate_literal(literal):
    """Niega un literal."""
    if isinstance(literal, str):
        return ("NOT", literal)
    elif isinstance(literal, tuple) and literal[0] == "NOT":
        return literal[1]
    return literal

def is_tautology(clause):
    """Verifica si una cláusula es una tautología (contiene P y ¬P)."""
    for lit in clause:
        if negate_literal(lit) in clause:
            return True
    return False

def resolve_pair(clause1, clause2):
    """Aplica resolución entre dos cláusulas. Retorna una lista de resolventes."""
    resolvents = []
    
    # Buscar literales complementarios
    for lit1 in clause1:
        negated = negate_literal(lit1)
        if negated in clause2:
            # Crear el resolvente eliminando los literales complementarios
            new_clause = (clause1 - {lit1}) | (clause2 - {negated})
            
            # Descartar tautologías
            if not is_tautology(new_clause):
                resolvents.append(frozenset(new_clause))
            
            # Solo resolver un par de literales por vez (resolución unitaria)
            break
    
    return resolvents

def resolution(clauses, max_iterations=1000, max_clauses=5000):
    """
    Algoritmo de resolución optimizado para CNF.
    Retorna True si KB ∧ ¬query es insatisfacible (es decir, KB ⊨ query).
    """
    clauses = set([frozenset(c) for c in clauses])
    
    # Si hay una cláusula vacía desde el inicio, hay contradicción
    if frozenset() in clauses:
        return True
    
    iterations = 0
    while iterations < max_iterations:
        iterations += 1
        
        # Priorizar cláusulas unitarias (con un solo literal) para eficiencia
        unit_clauses = [c for c in clauses if len(c) == 1]
        other_clauses = [c for c in clauses if len(c) > 1]
        
        new = set()
        
        # Primero resolver cláusulas unitarias entre sí
        if unit_clauses:
            for i, unit1 in enumerate(unit_clauses):
                # Resolver con otras cláusulas unitarias
                for unit2 in unit_clauses[i+1:]:
                    resolvents = resolve_pair(set(unit1), set(unit2))
                    for resolvent in resolvents:
                        if len(resolvent) == 0:
                            return True  # Cláusula vacía = contradicción
                        new.add(resolvent)
                
                # Resolver con cláusulas no unitarias
                for other in other_clauses:
                    resolvents = resolve_pair(set(unit1), set(other))
                    for resolvent in resolvents:
                        if len(resolvent) == 0:
                            return True  # Cláusula vacía = contradicción
                        new.add(resolvent)
        
        # Luego resolver entre cláusulas más pequeñas
        clause_list = sorted(other_clauses, key=len)[:100]  # Limitar a las 100 más pequeñas
        
        for i in range(len(clause_list)):
            for j in range(i + 1, min(i + 20, len(clause_list))):  # Solo comparar con vecinos cercanos
                resolvents = resolve_pair(set(clause_list[i]), set(clause_list[j]))
                
                for resolvent in resolvents:
                    if len(resolvent) == 0:
                        return True  # Cláusula vacía = contradicción
                    new.add(resolvent)
        
        # Si no hay nuevas cláusulas, no se puede derivar contradicción
        if not new or new.issubset(clauses):
            return False
        
        # Limitar el tamaño del conjunto de cláusulas
        clauses = clauses | new
        if len(clauses) > max_clauses:
            # Mantener solo las cláusulas más pequeñas (más útiles)
            clauses = set(sorted(clauses, key=len)[:max_clauses])
    
    # Si alcanzamos el límite sin encontrar contradicción
    return False

def entails(KB, query):
    """Returns True if KB entails query using CNF and resolution."""
    # Convertir KB y query a CNF
    KB_cnf = to_cnf(KB)
    
    # Para verificar si KB ⊨ query, verificamos si KB ∧ ¬query es insatisfacible
    negated_query = ("NOT", query)
    combined = ("AND", KB_cnf, to_cnf(negated_query))
    combined_cnf = to_cnf(combined)
    
    # Convertir a cláusulas
    clauses = to_clauses(combined_cnf)
    
    # Aplicar resolución
    return resolution(clauses)

def expr_to_string(expr, indent=0):
    """Convierte una expresión lógica (en formato de tuplas) a notación proposicional legible."""
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
    """Muestra la base de conocimiento en notación lógica proposicional y su conversión a CNF."""
    print("\n" + "="*70)
    print("BASE DE CONOCIMIENTO (Knowledge Base)")
    print("="*70)
    print("\nReglas en lógica proposicional (Original):")
    print("-"*70)
    print(expr_to_string(KB))
    
    print("\n" + "-"*70)
    print("Conversión a CNF (Conjunctive Normal Form):")
    print("-"*70)
    KB_cnf = to_cnf(KB)
    print(expr_to_string(KB_cnf))
    
    print("-"*70)
    print(f"Símbolos totales: {len(symbols_in(KB))}")
    print(f"Símbolos: {', '.join(sorted(symbols_in(KB)))}")
    print("="*70 + "\n")
