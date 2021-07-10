from . import pieces

class Pawn(pieces.Piece):
    # This is the piece class for the pawn.
    # It inherits from the Piece() parent class in pieces.py

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
    
    def legal_moves(self, current_board):
        legal_squares = []

        if self.color == 1:
            one_step_allowed = True
            two_steps_allowed = True

            capture_left_allowed = False
            capture_right_allowed = False

            for each in current_board:
                if self.x == each.x and self.y + 1 == each.y:
                    one_step_allowed = False
                if self.x == each.x and self.y + 2 == each.y:
                    two_steps_allowed = False
                
                if self.x - 1 == each.x and self.y + 1 == each.y:
                    capture_left_allowed = True
                if self.x + 1 == each.x and self.y + 1 == each.y:
                    capture_right_allowed = True

            if one_step_allowed:
                legal_squares.append([self.x, self.y + 1])
            if self.previous_moves == [] and one_step_allowed and two_steps_allowed:
                legal_squares.append([self.x, self.y + 2])

            if capture_left_allowed:
                legal_squares.append([self.x - 1, self.y + 1])
            if capture_right_allowed:
                legal_squares.append([self.x + 1, self.y + 1])


        elif self.color == 0:
            one_step_allowed = True
            two_steps_allowed = True

            capture_left_allowed = False
            capture_right_allowed = False

            for each in current_board:
                if self.x == each.x and self.y - 1 == each.y:
                    one_step_allowed = False
                if self.x == each.x and self.y - 2 == each.y:
                    two_steps_allowed = False
                
                if self.x - 1 == each.x and self.y - 1 == each.y:
                    capture_left_allowed = True
                if self.x + 1 == each.x and self.y - 1 == each.y:
                    capture_right_allowed = True

            if one_step_allowed:
                legal_squares.append([self.x, self.y - 1])
            if self.previous_moves == [] and one_step_allowed and two_steps_allowed:
                legal_squares.append([self.x, self.y - 2])

            if capture_left_allowed:
                legal_squares.append([self.x - 1, self.y - 1])
            if capture_right_allowed:
                legal_squares.append([self.x + 1, self.y - 1])

        return legal_squares

    def en_passant(self, current_board):
        pass

    def reset(self, x, y):
        self.x = x
        self.y = y

        self.previous_moves = []