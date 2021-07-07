import pieces

class Rook(pieces.Piece):
    # This is the piece class for the rook.
    # It inherits from the Piece() parent class in pieces.py

    def __init__(self, x, y, color):
        super().__init__(self, x, y, color)
    
    def legal_moves(self, current_board):
        pass

    def reset(self, x, y):
        self.x = x
        self.y = y

        self.previous_moves = []