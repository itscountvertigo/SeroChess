def move_to_coords(move):
    if move == "SHORT_CASTLE" or move == "LONG_CASTLE":
        return [None, move]

    old_x = ord(move[0]) - 97
    old_y = int(move[1]) - 1
    
    new_x = ord(move[2]) - 97
    new_y = int(move[3]) - 1

    return [[old_x, old_y], [new_x, new_y]]

def coords_to_move(old_x, old_y, x, y):
    return chr(ord('`')+(old_x + 1)) + str(old_y + 1) + chr(ord('`')+(x + 1)) + str(y + 1)

def coords_to_notation(old_x, old_y, new_x, new_y, piece, occupied, current_board):
    # This is a function that generates move text in the classic/standard chess notation.
    # This should not be used in the main list of moves.

    move_num_txt = str(current_board.move_num) + "." if piece.color == 1 else str(current_board.move_num) + "..."
    piece_char = piece.piece_character
    
    capture_char = ''
    if piece.__class__.__name__ == 'Pawn' and occupied == 1:
        capture_char += f"{chr(ord('`')+(old_x + 1))}"
    if occupied == 1:
        capture_char += 'x'
    
    location = chr(ord('`')+(new_x + 1)) + str(new_y + 1)
    checkmate_char = ''

    return f"{move_num_txt} {piece_char}{capture_char}{location}{checkmate_char}"