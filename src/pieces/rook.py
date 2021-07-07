from . import pieces

class Rook(pieces.Piece):
    # This is the piece class for the rook.
    # It inherits from the Piece() parent class in pieces.py
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
    
    def legal_moves(self):
        legal_squares = []

        for x in range(8):
            if x == self.x:
                continue
            legal_squares.append([x, self.y])

        for y in range(8):
            if y == self.y:
                continue
            legal_squares.append([self.x, y])
        
        return legal_squares

    def reset(self, x, y):
        self.x = x
        self.y = y

        self.previous_moves = []