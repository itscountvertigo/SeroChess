class Piece:
    # This is the parent class for all piece subclasses. 
    # All piece classes inherit from Piece().

    def __init__(self, x: int, y: int, color: int):
        self.x = x
        self.y = y
        self.color = color  # 0 for black, 1 for white

        self.selecting_squares = False

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_color(self):
        return self.color

    def description(self):
        # creates clean string for which color the piece is
        b_or_w = "Black" if self.color == 0 else "White"

        # gets class name (eg. "King" or "Bishop")
        class_name = self.__class__.__name__.lower()

        # "chr(ord('`') + number)" converts number to corresponding (lowercase) letter in alphabet
        location = chr(ord('`')+(self.x+1)) + str(self.y + 1)

        return "{} {} on {} ({}=[{}, {}])".format(b_or_w, class_name, location, location, self.x, self.y)
