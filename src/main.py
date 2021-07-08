from pieces import king, queen, rook, knight, bishop, pawn

board = []

board.append(king.King(4, 0, 1)) # white's king
board.append(queen.Queen(3, 0, 1)) # white's queen
board.append(bishop.Bishop(2, 0, 1)) # white's dark square bishop
board.append(bishop.Bishop(5, 0, 1)) # white's light square bishop
board.append(knight.Knight(1, 0, 1)) # whites knight that starts on b
board.append(knight.Knight(6, 0, 1)) # white's knight that starts on g
board.append(rook.Rook(0, 0, 1)) # white's rook that starts on a
board.append(rook.Rook(7, 0, 1)) # white's rook that starts on h

board.append(king.King(4, 7, 0)) # black's king
board.append(queen.Queen(3, 7, 0)) # black's queen
board.append(bishop.Bishop(2, 7, 0)) # black's dark square bishop
board.append(bishop.Bishop(5, 7, 0)) # black's light square bishop
board.append(knight.Knight(1, 7, 0)) # blacks knight that starts on b
board.append(knight.Knight(6, 7, 0)) # black's knight that starts on g
board.append(rook.Rook(0, 7, 0)) # black's rook that starts on a
board.append(rook.Rook(7, 7, 0)) # white's rook that starts on h

for i in range(8):
    board.append(pawn.Pawn(i, 1, 1))
    board.append(pawn.Pawn(i, 6, 0))