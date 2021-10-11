def all_legal_moves(board, side):
    all_legal_moves = []
    for piece in board:
        if piece.color == side:
            all_legal_moves += piece.legal_moves(board)

    return all_legal_moves