from . import pieces

class Queen(pieces.Piece):
    # This is the piece class for the queen.
    # It inherits from the Piece() parent class in pieces.py
    
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def legal_moves(self):
        legal_squares = []

        # moves horizontally/vertically
        for x in range(8):
            if x == self.x:
                continue
            legal_squares.append([x, self.y])

        for y in range(8):
            if y == self.y:
                continue
            legal_squares.append([self.x, y])
        
        # moves diagonally
        # find points on diagonal pointing up (white's perspective)
        for i in range(-8, 8):
            point_x = self.x + i
            point_y = self.y + i

            if (point_x < 0 or point_x > 7) or (point_y < 0 or point_y > 7):
                continue
            elif point_x == self.x:
                continue
            else:
                legal_squares.append([point_x, point_y])

        # find points on diagonal pointing down (white's perspective)
        for i in range(-8, 8):
            point_x = self.x + i
            point_y = self.y - i

            if (point_x < 0 or point_x > 7) or (point_y < 0 or point_y > 7):
                continue
            elif point_x == self.x:
                continue
            else:
                legal_squares.append([point_x, point_y])

        return legal_squares

    def reset(self, x, y):
        self.x = x
        self.y = y

        self.previous_moves = []