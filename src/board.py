from pieces import king, queen, rook, knight, bishop, pawn

import move_coords
from fen_import import read_FEN

class Board():
    def __init__(self, position, who_to_move, move_num, ply, moves):
        self.pieces = position
        self.who_to_move = who_to_move

        self.move_num = move_num
        self.moves = moves

        self.ply = ply
    
    def move(self, move):
        if move == "SHORT_CASTLE":
            for piece in self.pieces:
                if piece.__class__.__name__ == "King" and piece.color == self.who_to_move:
                    piece.x = 6

                if piece.__class__.__name__ == "Rook" and piece.color == self.who_to_move and piece.x == 7:
                    piece.x = 5

            if piece.color == 0:
                self.move_num += 1
            self.ply += 1

            return

        if move == "LONG_CASTLE":
            for piece in self.pieces:
                if piece.__class__.__name__ == "King" and piece.color == self.who_to_move:
                    piece.x = 2

                print(piece.__class__.__name__, piece.color, piece.x)

                if piece.__class__.__name__ == "Rook" and piece.color == self.who_to_move and piece.x == 0:
                    print("here")
                    piece.x = 3

            if piece.color == 0:
                self.move_num += 1
            self.ply += 1

            return

        coords = move_coords.move_to_coords(move)
        old_coords = coords[0]
        new_coords = coords[1]

        for piece in self.pieces:
            if [piece.x, piece.y] == old_coords:
                piece.x = new_coords[0]
                piece.y = new_coords[1]

                break
        
        if piece.color == 0:
            self.move_num += 1
        self.ply += 1

# def starting_position():
#     starting_position = [king.King(4, 0, 1),                              # white king
#                          queen.Queen(3, 0, 1),                            # white queen
#                          bishop.Bishop(2, 0, 1), bishop.Bishop(5, 0, 1),  # white bishops
#                          knight.Knight(1, 0, 1), knight.Knight(6, 0, 1),  # white knights
#                          rook.Rook(0, 0, 1), rook.Rook(7, 0, 1),          # white rooks
#                          king.King(4, 7, 0),                              # black king
#                          queen.Queen(3, 7, 0),                            # black queen
#                          bishop.Bishop(2, 7, 0), bishop.Bishop(5, 7, 0),  # black bishops
#                          knight.Knight(1, 7, 0), knight.Knight(6, 7, 0),  # black knights
#                          rook.Rook(0, 7, 0), rook.Rook(7, 7, 0)           # black rooks
#                         ]

#     for i in range(8):
#         starting_position.append(pawn.Pawn(i, 1, 1))
#         starting_position.append(pawn.Pawn(i, 6, 0))

#     return starting_position

main_board = Board(read_FEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"), 1, 1, 0, [])