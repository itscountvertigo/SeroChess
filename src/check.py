import legal_moves_list
import move_coords

def check(current_board, side):
    opponent_legal_moves = legal_moves_list.all_legal_moves(current_board.pieces, not side)

    for piece in current_board.pieces:
        if piece.__class__.__name__ == "King" and piece.color == side:
            for move in opponent_legal_moves:
                if move_coords.move_to_coords(move)[1] == [piece.x, piece.y]:
                    return True
    return False

def mate(current_board, side):
    pass