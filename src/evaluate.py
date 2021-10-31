from piece_heatmap import bishop_map, king_map, knight_map

def evaluate(current_board):
    white_value = count_material(current_board, 1)
    black_value = count_material(current_board, 0)

    evaluation = white_value - black_value

    for piece in current_board.pieces:
        piece_type = piece.__class__.__name__
        if piece_type == 'Pawn':
            pass
        
        elif piece_type == 'Knight':
            if piece.color == 1:
                evaluation += knight_map.white[piece.y][piece.x] * (piece.piece_value / 3)
            else:
                evaluation -= knight_map.black[piece.y][piece.x] * (piece.piece_value / 3)
        
        elif piece_type == 'Bishop':
            if piece.color == 1:
                evaluation += bishop_map.white[piece.y][piece.x] * (piece.piece_value / 3)
            else:
                evaluation -= bishop_map.black[piece.y][piece.x] * (piece.piece_value / 3)
        
        elif piece_type == 'Rook':
            pass
        
        elif piece_type == 'Queen':
            # temporarily use knight map until i have a queen map
            if piece.color == 1:
                evaluation += knight_map.white[piece.y][piece.x]  * (piece.piece_value / 3)
            else:
                evaluation -= knight_map.black[piece.y][piece.x]  * (piece.piece_value / 3)

        elif piece_type == 'King':
            if piece.color == 1:
                evaluation += king_map.white[piece.y][piece.x]
                # print("white king value: " + str(king_map.white[piece.x][piece.y]))
            else:
                evaluation -= king_map.black[piece.y][piece.x]
                # print("black king value: " + str(king_map.black[piece.x][piece.y]))

    return round(evaluation, 5)
    
def count_material(current_board, color):
    material_value = 0

    for piece in current_board.pieces:
        if piece.color == color:
            material_value += piece.piece_value

    return material_value