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

    def description(self):
        location = chr(ord('`')+(self.x+1)) + str(self.y + 1) # chr(ord('`') + number) converts number to corresponding letter in alphabet
        b_or_w = "Black's" if self.color == 0 else "White's"
        class_name = self.__class__.__name__.lower()
        return "{} {} on {}".format(b_or_w, class_name, location)