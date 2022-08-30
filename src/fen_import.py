from pieces import king, queen, rook, bishop, knight, pawn

def read_FEN(FEN_code):
    output_FEN = []
    x = 0
    y = 7

    for char in FEN_code:
        if y >- 1 and x < 9:
            if char == '/':
                x = 0
                y -= 1

            # black pieces
            elif char == 'r':
                output_FEN.append(rook.Rook(x, y, 0))
                x += 1
            elif char == 'n':
                output_FEN.append(knight.Knight(x, y, 0))
                x += 1
            elif char == 'b':
                output_FEN.append(bishop.Bishop(x, y, 0))
                x += 1
            elif char == 'q':
                output_FEN.append(queen.Queen(x, y, 0))
                x += 1
            elif char == 'k':
                output_FEN.append(king.King(x, y, 0))
                x += 1
            elif char == 'p':
                output_FEN.append(pawn.Pawn(x, y, 0))
                x += 1

            # white pieces
            elif char == 'R':
                output_FEN.append(rook.Rook(x, y, 1))
                x += 1
            elif char == 'N':
                output_FEN.append(knight.Knight(x, y, 1))
                x += 1
            elif char == 'B':
                output_FEN.append(bishop.Bishop(x, y, 1))
                x += 1
            elif char == 'Q':
                output_FEN.append(queen.Queen(x, y, 1))
                x += 1
            elif char == 'K':
                output_FEN.append(king.King(x, y, 1))
                x += 1
            elif char == 'P':
                output_FEN.append(pawn.Pawn(x, y, 1))
                x += 1
            elif char == ' ':
                y -= 1
            else:
                for j in range(48,57):
                    if char == chr(j):
                        x += j - 48
        #print(X)
    return output_FEN