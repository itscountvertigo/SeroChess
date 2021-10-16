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
            self.sprite_path = "src/sprites/black/black_knight.png"
        else:
            self.sprite_path = "src/sprites/white/white_knight.png"
 
    def legal_moves(self, current_board):
        legal_squares = [[self.x + 1, self.y + 2], [self.x - 1, self.y + 2],  # up 2, 1 left/right
                         [self.x + 2, self.y + 1], [self.x - 2, self.y + 1],  # up 1, 2 left/right
                         [self.x + 2, self.y - 1], [self.x - 2, self.y - 1],  # down 1, 2 left/right
                         [self.x - 1, self.y - 2], [self.x + 1, self.y - 2]   # down 2, 1 left/right
                         ]

        remove_list = []
        for i in legal_squares:
            if i[0] < 0 or i[1] < 0:
                remove_list.append(i)
            for each in current_board:
                if i[0] == each.x and i[1] == each.y and each.color == self.color:
                    remove_list.append(i)

        for x in remove_list:
            legal_squares.remove(x)

        legal_moves = []
        for each in legal_squares:
            legal_moves.append(move_coords.coords_to_move(self.x, self.y, each[0], each[1]))
            # legal_moves.append(chr(ord('`')+(self.x + 1)) + str(self.y + 1) + chr(ord('`')+(each[0] + 1)) + str(each[1] + 1))

        return legal_moves

    def reset(self, x, y):
        self.x = x
        self.y = y

        self.previous_moves = []