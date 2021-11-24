from . import pieces

import move_coords

class Knight(pieces.Piece):
    # This is the piece class for the knight.
    # It inherits from the Piece() parent class in pieces.py

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.piece_value = 3
        self.piece_character = 'N'

        if color == 0:
            self.sprite_path = "assets/default_sprites/black/black_knight.png"
        else:
            self.sprite_path = "assets/default_sprites/white/white_knight.png"
 
    def legal_moves(self, current_board):
        legal_squares = []

        for x in range(-2,2):
            if x == 0:
                continue
            y_diff = 1 if x % 2 == 0 else 2
            if self.x + x >= 0 and self.x + x <= 7:
                if self.y + y_diff >= 0 and self.y + y_diff <= 7:
                    if self.check_occupied(self.x + x, self.y + y_diff, current_board) != 2:
                        legal_squares.append([self.x + x, self.y + y_diff])

                if self.y - y_diff >= 0 and self.y - y_diff <= 7:
                   if self.check_occupied(self.x + x, self.y - y_diff, current_board) != 2:
                        legal_squares.append([self.x + x, self.y - y_diff])

        # print(legal_squares)

        legal_moves = []
        for each in legal_squares:
            legal_moves.append(move_coords.coords_to_move(self.x, self.y, each[0], each[1]))

        return legal_moves

    def reset(self, x, y):
        self.x = x
        self.y = y

        self.previous_moves = []