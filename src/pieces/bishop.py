from . import pieces

import move_coords

class Bishop(pieces.Piece):
    # This is the piece class for the bishop.
    # It inherits from the Piece() parent class in pieces.py

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.piece_value = 3
        self.piece_character = 'B'

        if color == 0:
            self.sprite_path = "src/sprites/black/black_bishop.png"
        else:
            self.sprite_path = "src/sprites/white/white_bishop.png"
    
    def legal_moves(self, current_board):
        legal_squares = []

        for tl in range(8):
            point_x = self.x - tl
            point_y = self.y + tl

            if point_x == self.x:
                continue
            if point_x < 0 or point_y < 0:
                break
            if point_x > 7 or point_y > 7:
                break

            occupied = self.check_occupied(point_x, point_y, current_board)

            if occupied == 2:
                break
            elif occupied == 1:
                legal_squares.append([point_x, point_y])
                break
            else:
                legal_squares.append([point_x, point_y])

        for tr in range(8):
            point_x = self.x + tr
            point_y = self.y + tr

            if point_x == self.x:
                continue
            if point_x < 0 or point_y < 0:
                break
            if point_x > 7 or point_y > 7:
                break

            occupied = self.check_occupied(point_x, point_y, current_board)

            if occupied == 2:
                break
            elif occupied == 1:
                legal_squares.append([point_x, point_y])
                break
            else:
                legal_squares.append([point_x, point_y])

        for bl in range(8):
            point_x = self.x - bl
            point_y = self.y - bl

            if point_x == self.x:
                continue
            if point_x < 0 or point_y < 0:
                break
            if point_x > 7 or point_y > 7:
                break

            occupied = self.check_occupied(point_x, point_y, current_board)

            if occupied == 2:
                break
            elif occupied == 1:
                legal_squares.append([point_x, point_y])
                break
            else:
                legal_squares.append([point_x, point_y])

        for br in range(8):
            point_x = self.x + br
            point_y = self.y - br

            if point_x == self.x:
                continue
            if point_x < 0 or point_y < 0:
                break
            if point_x > 7 or point_y > 7:
                break

            occupied = self.check_occupied(point_x, point_y, current_board)

            if occupied == 2:
                break
            elif occupied == 1:
                legal_squares.append([point_x, point_y])
                break
            else:
                legal_squares.append([point_x, point_y])

        legal_moves = []
        for each in legal_squares:
            legal_moves.append(move_coords.coords_to_move(self.x, self.y, each[0], each[1]))
            # legal_moves.append(chr(ord('`')+(self.x + 1)) + str(self.y + 1) + chr(ord('`')+(each[0] + 1)) + str(each[1] + 1))

        return legal_moves

    def reset(self, x, y):
        self.x = x
        self.y = y

        self.previous_moves = []
