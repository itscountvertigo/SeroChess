from . import pieces

class Knight(pieces.Piece):
    # This is the piece class for the knight.
    # It inherits from the Piece() parent class in pieces.py

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
 
    def legal_moves(self):
        legal_squares = []

        legal_squares.append([self.x + 1, self.y + 2]) # up 2, 1 right (as all following comments, from white's perspective)
        legal_squares.append([self.x + 1, self.y - 2]) # down 2, 1 right

        legal_squares.append([self.x - 1, self.y + 2]) # up 2, 1 left

        legal_squares.append([self.x + 2, self.y + 1]) # up 1, 2 right
        legal_squares.append([self.x - 2, self.y + 1]) # up 1, 2 left

        legal_squares.append([self.x + 2, self.y - 1]) # down 1, 2 right
        legal_squares.append([self.x - 2, self.y - 1]) # down 1, 2 left
        
        legal_squares.append([self.x - 1, self.y - 2]) # down 2, 1 left

        remove_list = []
        for x in legal_squares:
            if x[0] < 0 or x[1] < 0:
                remove_list.append(x)

        for x in remove_list:
            legal_squares.remove(x)

        return legal_squares

    def reset(self, x, y):
        self.x = x
        self.y = y

        self.previous_moves = []