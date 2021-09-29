from . import pieces

class Knight(pieces.Piece):
    # This is the piece class for the knight.
    # It inherits from the Piece() parent class in pieces.py

    def __init__(self, x, y, color):
        super().__init__(x, y, color)

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

        return legal_squares

    def reset(self, x, y):
        self.x = x
        self.y = y

        self.previous_moves = []