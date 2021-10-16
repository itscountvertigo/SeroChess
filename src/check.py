import legal_moves_list
import move_coords

def check(board, side):
    opponent_legal_moves = legal_moves_list.all_legal_moves(board, not side)

    for piece in board:
        if piece.__class__.__name__ == "King" and piece.color == side:
            for move in opponent_legal_moves:
                # print(f"move txt: {move}\ncoords: {move_coords.move_to_coords(move)}\n king coords: {[piece.x, piece.y]}\n\n")
                if move_coords.move_to_coords(move) == [piece.x, piece.y]:
                    return True
    return False