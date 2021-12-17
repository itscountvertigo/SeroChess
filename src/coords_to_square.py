def coords_to_square(x, y, width):
    border_values = []
    for i in range(8):
        border_values.append(width / 8 * i)
    
    square_x = 7
    square_y = 7

    for i in border_values:
        if x < i:
            square_x = int(i / (width / 8) - 1)
            break

    for i in border_values:
        if y < i:
            square_y = int(i / (width / 8) - 1)
            break

    return (square_x, square_y)