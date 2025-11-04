def minimax(board, jugador):
    if terminal(board):
        return utilidad(board)  # +1, 0 o -1

    if jugador == "X":  # MAX
        mejor = -float("inf")
        for movimiento in movimientos_posibles(board):
            valor = minimax(aplicar(board, movimiento, "O"))
            mejor = max(mejor, valor)
        return mejor
    else:  # MIN
        mejor = float("inf")
        for movimiento in movimientos_posibles(board):
            valor = minimax(aplicar(board, movimiento, "X"))
            mejor = min(mejor, valor)
        return mejor