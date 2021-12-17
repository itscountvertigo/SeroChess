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
        coords = move_coords.move_to_coords(move)
        old_coords = coords[0]
        new_coords = coords[1]

        removed_piece = None

        for piece in self.pieces:
            if (piece.x, piece.y) == new_coords:
                removed_piece = piece

            if (piece.x, piece.y) == old_coords:
                piece_type = piece.__class__.__name__
                        
                # making in_starting_position (check for en passant / castling) false
                if piece_type == "Pawn" or piece_type == "King" or piece_type == "Rook":
                    piece.in_starting_position = False
                    # en passant capturing
                    if piece_type == 'Pawn' and (piece.enemy_en_passant_left or piece.enemy_en_passant_right):
                        for i in self.pieces:
                            if i == piece.enemy_en_passant_left:
                                self.pieces.remove(i)
                            elif i == piece.enemy_en_passant_right:
                                self.pieces.remove(i)

                # Move the piece
                piece.x = new_coords[0]
                piece.y = new_coords[1]

        if removed_piece:
            self.pieces.remove(removed_piece)

        self.moves.append(move)
        
        if self.who_to_move == 0:
            self.move_num += 1
        self.ply += 1

        self.who_to_move = not self.who_to_move

    def check_square_occupied(self, x, y, color):
        """
        Returns a value of 0, 1 or 2 depending on wether it's: 
        - 0: completely free
        - 1: occupied by an opponent piece (capture)
        - 2: occupied by a friendly piece (blocked)
        """

        for each in self.pieces:
            if each.x == x and each.y == y:
                if each.color == color:
                    # A friendly piece blocks the square
                    return 2
                else:
                    # An enemy piece occupies the square (it can be captured)
                    return 1
        
        # There aren't any pieces on the square
        return 0

main_board = Board(read_FEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"), 1, 1, 0, [])
# main_board = Board(read_FEN("7k/7r/6r1/K7/8/8/8/8 b KQkq - 0 1"), 0, 1, 0, []) # mate in 2 puzzle