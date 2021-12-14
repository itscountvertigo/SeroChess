def all_legal_moves(board, side):
    all_legal_moves = []
    for piece in board.pieces:
        if piece.color == side:
            all_legal_moves.extend(piece.legal_moves(board))

    return all_legal_moves