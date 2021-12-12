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
                    

        """

        for each in self.pieces:
                if each.x == x and each.y == y:
                    if each.color == self.color:
                        capturing_piece = False
                        blocked_by_own_piece = True
                    else:
                        capturing_piece = True
                        blocked_by_own_piece = False

                    break
                else:
                    capturing_piece = False
                    blocked_by_own_piece = False

        # return values of the square. 0: square is free, 1: capturing, 2: blocked
        if capturing_piece:
            return 1
        elif blocked_by_own_piece:
            return 2
        else:
            return 0
        """

main_board = Board(read_FEN("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"), 1, 1, 0, [])