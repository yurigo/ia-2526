WINS = [(0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)]

def winner(b):
    for a,b_,c in WINS:
        if b[a] != " " and b[a] == b[b_] == b[c]:
            return b[a]
    return None

def terminal(b):
    return winner(b) is not None or all(c != " " for c in b)

def utility(b, me):
    w = winner(b)
    if w == me: return 1
    if w is None and terminal(b): return 0
    return -1  # gana el rival

def actions(b):
    return [i for i,c in enumerate(b) if c == " "]

def apply(b, i, p):
    nb = b[:]
    nb[i] = p
    return nb

def minimax(b, me, turn):
    if terminal(b):
        return utility(b, me), None
    if turn == me:
        best_val, best_move = -2, None
        for a in actions(b):
            val, _ = minimax(apply(b, a, turn), me, "O" if turn=="X" else "X")
            if val > best_val:
                best_val, best_move = val, a
        return best_val, best_move
    else:
        best_val, best_move = 2, None
        for a in actions(b):
            val, _ = minimax(apply(b, a, turn), me, "O" if turn=="X" else "X")
            if val < best_val:
                best_val, best_move = val, a
        return best_val, best_move

# Demo
board = ["X", "O" , "X", "O", "O", " ", " ", " ", " "] 

me = "X"
val, move = minimax(board, me, "X")
print("Mejor movimiento para X:", move)