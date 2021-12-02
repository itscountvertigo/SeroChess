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
        """
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
        """

        coords = move_coords.move_to_coords(move)
        old_coords = coords[0]
        new_coords = coords[1]

        removed_piece = None

        for piece in self.pieces:
            if [piece.x, piece.y] == new_coords:
                removed_piece = piece

            if [piece.x, piece.y] == old_coords:
                piece.x = new_coords[0]
                piece.y = new_coords[1]

        if removed_piece:
            self.pieces.remove(removed_piece)
        
        if self.who_to_move == 0:
            self.move_num += 1
        self.ply += 1

        self.who_to_move = not self.who_to_move

    def check_square_occupied(x, y):
        pass

main_board = Board(read_FEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"), 1, 1, 0, [])