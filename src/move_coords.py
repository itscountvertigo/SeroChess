def move_to_coords(move):
    x = ord(move[2]) - 97
    y = int(move[3]) - 1

    return [x, y]

def coords_to_move(old_x, old_y, x, y):
    return chr(ord('`')+(old_x + 1)) + str(old_y + 1) + chr(ord('`')+(x + 1)) + str(y + 1)