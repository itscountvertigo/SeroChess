class Piece():
    # This is the parent class for all piece subclasses. 
    # All piece classes inherit from Piece().

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color # 0 for black, 1 for white

        self.previous_moves = []

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_color(self):
        return self.color