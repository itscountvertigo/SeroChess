from . import pieces

class Queen(pieces.Piece):
    # This is the piece class for the queen.
    # It inherits from the Piece() parent class in pieces.py
    
    def __init__(self, x, y, color):
        super().__init__(x, y, color)

    def legal_moves(self, current_board):
        legal_squares = []

        # Rook-like moves
        for left in range(8):
            point_x = self.x - left
            point_y = self.y

            if point_x == self.x:
                continue
            if point_x < 0 or point_y < 0:
                break
            if point_x > 7 or point_y > 7:
                break

            blocked_by_own_piece = False
            capturing_piece = False

            for each in current_board:
                if each.x == point_x and each.y == point_y:
                    if each.color == self.color:
                        capturing_piece = False
                        blocked_by_own_piece = True
                    else:
                        capturing_piece = True
                        blocked_by_own_piece = False

                    break
                else:
                    capturing_piece = False
                    blocked_by_own_piece = False

            if blocked_by_own_piece:
                break
            elif capturing_piece:
                legal_squares.append([point_x, point_y])
                break
            else:
                legal_squares.append([point_x, point_y])

        for right in range(8):
            point_x = self.x + right
            point_y = self.y

            if point_x == self.x:
                continue
            if point_x < 0 or point_y < 0:
                break
            if point_x > 7 or point_y > 7:
                break

            blocked_by_own_piece = False
            capturing_piece = False

            for each in current_board:
                if each.x == point_x and each.y == point_y:
                    if each.color == self.color:
                        capturing_piece = False
                        blocked_by_own_piece = True
                    else:
                        capturing_piece = True
                        blocked_by_own_piece = False

                    break
                else:
                    capturing_piece = False
                    blocked_by_own_piece = False

            if blocked_by_own_piece:
                break
            elif capturing_piece:
                legal_squares.append([point_x, point_y])
                break
            else:
                legal_squares.append([point_x, point_y])

        for up in range(8):
            point_x = self.x
            point_y = self.y + up

            if point_y == self.y:
                continue
            if point_x < 0 or point_y < 0:
                break
            if point_x > 7 or point_y > 7:
                break

            blocked_by_own_piece = False
            capturing_piece = False

            for each in current_board:
                if each.x == point_x and each.y == point_y:
                    if each.color == self.color:
                        capturing_piece = False
                        blocked_by_own_piece = True
                    else:
                        capturing_piece = True
                        blocked_by_own_piece = False

                    break
                else:
                    capturing_piece = False
                    blocked_by_own_piece = False

            if blocked_by_own_piece:
                break
            elif capturing_piece:
                legal_squares.append([point_x, point_y])
                break
            else:
                legal_squares.append([point_x, point_y])

        for down in range(8):
            point_x = self.x
            point_y = self.y - down

            if point_y == self.y:
                continue
            if point_x < 0 or point_y < 0:
                break
            if point_x > 7 or point_y > 7:
                break

            blocked_by_own_piece = False
            capturing_piece = False

            for each in current_board:
                if each.x == point_x and each.y == point_y:
                    if each.color == self.color:
                        capturing_piece = False
                        blocked_by_own_piece = True
                    else:
                        capturing_piece = True
                        blocked_by_own_piece = False

                    break
                else:
                    capturing_piece = False
                    blocked_by_own_piece = False

            if blocked_by_own_piece:
                break
            elif capturing_piece:
                legal_squares.append([point_x, point_y])
                break
            else:
                legal_squares.append([point_x, point_y])

        # Bishop-like moves
        for tl in range(8):
            point_x = self.x - tl
            point_y = self.y + tl

            if point_x == self.x:
                continue
            if point_x < 0 or point_y < 0:
                break
            if point_x > 7 or point_y > 7:
                break

            blocked_by_own_piece = False
            capturing_piece = False

            for each in current_board:
                if each.x == point_x and each.y == point_y:
                    if each.color == self.color:
                        capturing_piece = False
                        blocked_by_own_piece = True
                    else:
                        capturing_piece = True
                        blocked_by_own_piece = False

                    break
                else:
                    capturing_piece = False
                    blocked_by_own_piece = False

            if blocked_by_own_piece:
                break
            elif capturing_piece:
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

            blocked_by_own_piece = False
            capturing_piece = False

            for each in current_board:
                if each.x == point_x and each.y == point_y:
                    if each.color == self.color:
                        capturing_piece = False
                        blocked_by_own_piece = True
                    else:
                        capturing_piece = True
                        blocked_by_own_piece = False

                    break
                else:
                    capturing_piece = False
                    blocked_by_own_piece = False

            if blocked_by_own_piece:
                break
            elif capturing_piece:
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

            blocked_by_own_piece = False
            capturing_piece = False

            for each in current_board:
                if each.x == point_x and each.y == point_y:
                    if each.color == self.color:
                        capturing_piece = False
                        blocked_by_own_piece = True
                    else:
                        capturing_piece = True
                        blocked_by_own_piece = False

                    break
                else:
                    capturing_piece = False
                    blocked_by_own_piece = False

            if blocked_by_own_piece:
                break
            elif capturing_piece:
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

            blocked_by_own_piece = False
            capturing_piece = False

            for each in current_board:
                if each.x == point_x and each.y == point_y:
                    if each.color == self.color:
                        capturing_piece = False
                        blocked_by_own_piece = True
                    else:
                        capturing_piece = True
                        blocked_by_own_piece = False

                    break
                else:
                    capturing_piece = False
                    blocked_by_own_piece = False

            if blocked_by_own_piece:
                break
            elif capturing_piece:
                legal_squares.append([point_x, point_y])
                break
            else:
                legal_squares.append([point_x, point_y])

        return legal_squares

    def reset(self, x, y):
        self.x = x
        self.y = y

        self.previous_moves = []