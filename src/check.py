import legal_moves_list
import move_coords

def check(board, side):
    target_king = None
    for piece in board:
        if piece.__class__.__name__ == "King" and piece.color == side:
            target_king = piece
            print(target_king.x, target_king.y)
            break

    if not target_king:
        return

    for move in legal_moves_list.all_legal_moves(board, side):
        # print(move_coords.move_to_coords(move), [target_king.x, target_king.y])
        if move_coords.move_to_coords(move) == [target_king.x, target_king.y]:
            return True
    return False