import pieces.king as king
import pieces.queen as queen
import pieces.rook as rook
import pieces.knight as knight
import pieces.bishop as bishop
import pieces.pawn as pawn

def fen_import(fen_string):
    current_pos_x = 0
    current_pos_y = 7

    pieces_list = []

    for char in fen_string:
        if char == '/': 
            # move to next rank
            current_pos_x = 0
            current_pos_y -= 1
        elif char.isUpper():
            if char.lower() == 'k':
                king = king.King(current_pos_x, current_pos_y, 1)
                pieces_list.append(king)
