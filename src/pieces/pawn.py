from numpy import e
from . import pieces
import board

class Pawn(pieces.Piece):
    # This is the piece class for the pawn.
    # It inherits from the Piece() parent class in pieces.py

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.piece_value = 1
        self.piece_character = ''

        self.in_starting_position = True

        self.enemy_en_passant_left = None
        self.enemy_en_passant_right = None

        if color == 0:
            self.sprite_path = "src/sprites/black/black_pawn.png"
        else:
            self.sprite_path = "src/sprites/white/white_pawn.png"
    
    def legal_moves(self, current_board):
        legal_squares = []

        # self.enemy_en_passant_left = None
        # self.enemy_en_passant_right = None

        if self.color == 1:
            one_step_allowed = True
            two_steps_allowed = False

            if self.in_starting_position:
                two_steps_allowed = True

            capture_left_allowed = False
            capture_right_allowed = False

            for each in current_board:
                if self.x == each.x and self.y + 1 == each.y:
                    one_step_allowed = False
                    two_steps_allowed = False

                if self.x - 1 == each.x and self.y + 1 == each.y and self.color != each.color:
                    capture_left_allowed = True

                if self.x + 1 == each.x and self.y + 1 == each.y and self.color != each.color:
                    capture_right_allowed = True
            
            if two_steps_allowed == True:
                for each in current_board:
                    if self.x == each.x and self.y + 2 == each.y:
                        two_steps_allowed = False

            if one_step_allowed:
                legal_squares.append([self.x, self.y + 1])
                if two_steps_allowed:
                    legal_squares.append([self.x, self.y + 2])

            if capture_left_allowed:
                legal_squares.append([self.x - 1, self.y + 1])
            if capture_right_allowed:
                legal_squares.append([self.x + 1, self.y + 1])

            if board.moves:
                en_passant = self.en_passant(board.moves[-1])
                if en_passant[0]:
                    legal_squares.append([self.x - 1, self.y + 1])
                    for piece in current_board:
                        if piece.x == self.x - 1 and piece.y == self.y:
                            self.enemy_en_passant_left = piece

                elif en_passant[1]:
                    legal_squares.append([self.x + 1, self.y + 1])
                    for piece in current_board:
                        if piece.x == self.x + 1 and piece.y == self.y:
                            self.enemy_en_passant_right = piece

        elif self.color == 0:
            one_step_allowed = True
            two_steps_allowed = False

            if self.in_starting_position:
                two_steps_allowed = True

            capture_left_allowed = False
            capture_right_allowed = False

            for each in current_board:
                if self.x == each.x and self.y - 1 == each.y:
                    one_step_allowed = False
                    two_steps_allowed = False

                if self.x - 1 == each.x and self.y - 1 == each.y and self.color != each.color:
                    capture_left_allowed = True

                if self.x + 1 == each.x and self.y - 1 == each.y and self.color != each.color:
                    capture_right_allowed = True
            
            if two_steps_allowed == True:
                for each in current_board:
                    if self.x == each.x and self.y - 2 == each.y:
                        two_steps_allowed = False

            if one_step_allowed:
                legal_squares.append([self.x, self.y - 1])
                if two_steps_allowed:
                    legal_squares.append([self.x, self.y - 2])

            if capture_left_allowed:
                legal_squares.append([self.x - 1, self.y - 1])
            if capture_right_allowed:
                legal_squares.append([self.x + 1, self.y - 1])

            if board.moves:
                en_passant = self.en_passant(board.moves[-1])
                if en_passant[0]:
                    legal_squares.append([self.x - 1, self.y - 1])
                    for piece in current_board:
                        if piece.x == self.x - 1 and piece.y == self.y:
                            self.enemy_en_passant_left = piece

                if en_passant[1]:
                    legal_squares.append([self.x + 1, self.y - 1])
                    for piece in current_board:
                        if piece.x == self.x + 1 and piece.y == self.y:
                            self.enemy_en_passant_right = piece

        legal_moves = []
        for each in legal_squares:
            legal_moves.append(chr(ord('`')+(self.x + 1)) + str(self.y + 1) + chr(ord('`')+(each[0] + 1)) + str(each[1] + 1))

        return legal_moves

    def en_passant(self, last_move):
        en_passant_left = False
        en_passant_right = False

        if self.color == 1 and self.y == 4:
            prev_move_left = f"{chr(ord('`')+((self.x - 1) + 1)) + str((self.y + 2) + 1)}{chr(ord('`')+((self.x - 1) + 1)) + str(self.y + 1)}"
            prev_move_right = f"{chr(ord('`')+((self.x + 1) + 1)) + str((self.y + 2) + 1)}{chr(ord('`')+((self.x + 1) + 1)) + str(self.y + 1)}"

            # to left of pawn (from white's perspective)
            if last_move == prev_move_left:
                en_passant_left = True
            # to right of pawn
            elif last_move == prev_move_right:
                en_passant_right = True
        
        elif self.color == 0 and self.y == 3:
            prev_move_left = f"{chr(ord('`')+((self.x - 1) + 1)) + str((self.y - 2) + 1)}{chr(ord('`')+((self.x - 1) + 1)) + str(self.y + 1)}"
            prev_move_right = f"{chr(ord('`')+((self.x + 1) + 1)) + str((self.y - 2) + 1)}{chr(ord('`')+((self.x + 1) + 1)) + str(self.y + 1)}"

            # to left of pawn (from white's perspective)
            if last_move == prev_move_left:
                en_passant_left = True
            # to right of pawn
            elif last_move == prev_move_right:
                en_passant_right = True
        
        return (en_passant_left, en_passant_right)

    def reset(self, x, y):
        self.x = x
        self.y = y

        self.previous_moves = []