def evaluate(board):
    white_material_value = count_material(board, 1)
    black_material_value = count_material(board, 0)

    evaluation = white_material_value - black_material_value
    
def count_material(board, color):
    material_value = 0

    for piece in board:

        if piece.color == color:
            material_value += piece.piece_value