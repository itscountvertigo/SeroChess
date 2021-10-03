from . import pieces

class King(pieces.Piece):
    # This is the piece class for the king.
    # It inherits from the Piece() parent class in pieces.py

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.piece_value = 0
        self.piece_character = 'K'

        if color == 0:
            self.sprite_path = "src/sprites/black/black_king.png"
        else:
            self.sprite_path = "src/sprites/white/white_king.png"

        self.short_castle_allowed = None
        self.long_castle_allowed = None

    def legal_moves(self, current_board):
        legal_squares = [[self.x - 1, self.y - 1],  # bottom left
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
            for each in current_board:
                if i[0] == each.x and i[1] == each.y and each.color == self.color:
                    remove_list.append(i)

        for x in remove_list:
            legal_squares.remove(x)
        
        return legal_squares

    def castle_allowed(self, current_board):
        if not self.previous_moves:
            # todo: find rook locations, determine for each if short and long castle are allowed
            pass

        else:
            # if king has moved, castling isnt allowed at all
            self.short_castle_allowed = False
            self.long_castle_allowed = False

    def reset(self, x, y):
        self.x = x
        self.y = y
        
        self.previous_moves = []

        self.short_castle_allowed = True
        self.long_castle_allowed = True