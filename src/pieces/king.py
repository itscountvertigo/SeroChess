from . import pieces

import move_coords
class King(pieces.Piece):
    # This is the piece class for the king.
    # It inherits from the Piece() parent class in pieces.py

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.piece_value = 999
        self.piece_character = 'K'

        if color == 0:
            self.sprite_path = "assets/default_sprites/black/black_king.png"
        else:
            self.sprite_path = "assets/default_sprites/white/white_king.png"

        self.in_starting_position = True

    def legal_moves(self, current_board):
        legal_squares = [
            [self.x - 1, self.y - 1],  # bottom left
            [self.x - 1, self.y],      # left
            [self.x - 1, self.y + 1],  # top left
            [self.x, self.y - 1],      # down
            [self.x, self.y + 1],      # up
            [self.x + 1, self.y - 1],  # bottom right
            [self.x + 1, self.y],      # right
            [self.x + 1, self.y + 1]   # top right
        ]

        remove_list = []
        for i in legal_squares:
            if i[0] < 0 or i[1] < 0:
                remove_list.append(i)
            for each in current_board.pieces:
                if i[0] == each.x and i[1] == each.y and each.color == self.color:
                    remove_list.append(i)

        for x in remove_list:
            legal_squares.remove(x)

        legal_moves = []
        for each in legal_squares:
            legal_moves.append(move_coords.coords_to_move(self.x, self.y, each[0], each[1]))
            # legal_moves.append(chr(ord('`')+(self.x + 1)) + str(self.y + 1) + chr(ord('`')+(each[0] + 1)) + str(each[1] + 1))
        """
        if self.short_castle_allowed(current_board):
            legal_moves.append("SHORT_CASTLE")
        if self.long_castle_allowed(current_board):
            legal_moves.append("LONG_CASTLE")
        """

        return legal_moves

    def short_castle_allowed(self, current_board):
        if not self.in_starting_position:
            # if king has moved, castling isnt allowed at all
            return False

        for piece in current_board.pieces:
            
            if (piece.x == 5 or piece.x == 6) and piece.y == 0 if self.color == 1 else 7:
                return False

            if piece.__class__.__name__ == "Rook" and piece.color == self.color:
                    if piece.x != 7 or piece.y != (0 if self.color == 1 else 7) or not piece.in_starting_position:
                        return False

            return True

    def long_castle_allowed(self, current_board):
        if not self.in_starting_position:
            # if king has moved, castling isnt allowed at all
            return False

        for piece in current_board.pieces:
            if piece.__class__.__name__ == "Rook" and piece.color == self.color:
                if self.color == 1:
                    if piece.x != 0 or piece.y != 0 or not piece.in_starting_position:
                        return False
                else:
                    if piece.x != 0 or piece.y != 7 or not piece.in_starting_position:
                        return False

            return True

    def reset(self, x, y):
        self.x = x
        self.y = y

        self.short_castle_allowed = True
        self.long_castle_allowed = True