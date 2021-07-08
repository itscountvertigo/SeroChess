from . import pieces

class Pawn(pieces.Piece):
    # This is the piece class for the pawn.
    # It inherits from the Piece() parent class in pieces.py

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
    
    def legal_moves(self):
        legal_squares = []

        if self.color == 1:
            legal_squares.append([self.x, self.y + 1])
            if self.previous_moves == []:
                legal_squares.append([self.x, self.y + 2])

        elif self.color == 0:
            legal_squares.append([self.x, self.y - 1])
            if self.previous_moves == []:
                legal_squares.append([self.x, self.y - 2])

        return legal_squares

    def en_passant(self, current_board):
        pass

    def reset(self, x, y):
        self.x = x
        self.y = y

        self.previous_moves = []