import board

def standard_notation(old_x, old_y, new_x, new_y, piece, occupied):
    move_num_txt = str(board.move_num) + "." if piece.color == 1 else str(board.move_num) + "..."
    piece_char = piece.piece_character
    
    capture_char = ''
    if piece.__class__.__name__ == 'Pawn' and occupied == 1:
        capture_char += f"{chr(ord('`')+(old_x + 1))}"
    if occupied == 1:
        capture_char += 'x'
    
    location = chr(ord('`')+(new_x + 1)) + str(new_y + 1)
    checkmate_char = ''

    return f"{move_num_txt} {piece_char}{capture_char}{location}{checkmate_char}"

def simplified(old_x, old_y, new_x, new_y):
    old_square = chr(ord('`')+(old_x + 1)) + str(old_y + 1)
    new_square = chr(ord('`')+(new_x + 1)) + str(new_y + 1)

    return f"{old_square}{new_square}"