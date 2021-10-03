import arcade

import board

import generate_move_text
from coords_to_square import coords_to_square

class GUI(arcade.Window):
    """
    The main class for the GUI. This class inherits from the arcade library.
    This is used to display the board.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # i stole lichess's palette
        self.color_w = [240, 217, 181]
        self.color_b = [181, 136, 99]

        self.selected_squares = []
        
        arcade.set_background_color(self.color_w)

    def on_draw(self):
        arcade.start_render()
        self.draw_squares(self.width / 8, self.height / 8)
        
        self.draw_sprites(board.pieces)

        # draw circles on the legal moves of a selected piece
        for each in self.selected_squares:
            arcade.draw_circle_filled(each[0] * self.width / 8 + self.width / 16, 
                                      each[1] * self.width / 8 + self.width / 16, 
                                      self.width / 32,
                                      [0, 0, 0, 30])

    def on_mouse_press(self, x, y, button, modifiers):
        coords = coords_to_square(x, y, self.width)

        for piece in board.pieces:
            # if clicked square has a piece:
            if piece.x == coords[0] and piece.y == coords[1] and board.who_to_move == piece.color:
                legal_moves = piece.legal_moves(board.pieces)

                # if the piece is not selected, remove others' and highlight this one's
                if not piece.selecting_squares:
                    self.selected_squares = []
                    for i in board.pieces:
                        i.selecting_squares = False

                    for i in legal_moves:
                        self.selected_squares.append(i)
                    piece.selecting_squares = True

                # if the piece is selected, unselect it (by emptying the selected squares array)
                else:
                    self.selected_squares = []
                    for i in board.pieces:
                        i.selecting_squares = False
            else:
                # if clicked square is one of a piece's selected and legal moves
                for square in self.selected_squares:
                    if coords[0] == square[0] and coords[1] == square[1] and piece.selecting_squares:
                        occupied = piece.check_occupied(coords[0], coords[1], board.pieces)

                        # formatted_move_notation = generate_move_text.standard_notation(piece.x, piece.y, coords[0], coords[1], piece, occupied)
                        formatted_move = generate_move_text.simplified(piece.x, piece.y, coords[0], coords[1])

                        piece.move(square[0], square[1])
                        board.moves.append(formatted_move)

                        # capturing
                        if occupied == 1: # 1 means there is a piece and it can be captured
                            for i in board.pieces:
                                if coords[0] == i.x and coords[1] == i.y and i != piece:
                                    board.pieces.remove(i)
                        
                        piece_type = piece.__class__.__name__

                        # en passant capturing
                        if piece_type == 'Pawn':
                            for i in board.pieces:
                                if i == piece.enemy_en_passant_left:
                                    board.pieces.remove(i)
                                elif i == piece.enemy_en_passant_right:
                                    board.pieces.remove(i)
                        
                        # making in_starting_position (check for en passant / castling) false
                        if piece_type == 'Pawn' or piece_type == 'King' or piece_type == 'Rook':
                            piece.in_starting_position = False

                        # change move num after black moves: one 'move' in chess means one move (ply) by each player
                        if piece.color == 0:
                            board.move_num += 1
                        board.ply += 1

                        # switch whose turn it is
                        board.who_to_move = not board.who_to_move
                        
                        self.selected_squares = []
                        for i in board.pieces:
                            i.selecting_squares = False

    def draw_squares(self, square_width, square_height):
        for x in range(8):
            for y in range(8):
                if x % 2 != y % 2:
                    arcade.draw_rectangle_filled(x * square_width + square_width / 2, 
                                                 y * square_height + square_height / 2, 
                                                 square_width, 
                                                 square_height, 
                                                 self.color_b)
    
    def draw_sprites(self, pieces):
        for each in pieces:
            new_sprite = arcade.Sprite(each.sprite_path,
                                       scale=1.2,
                                       center_x=(each.x * self.width / 8 + self.width / 16), 
                                       center_y=(each.y * self.height / 8 + self.width / 16))
            arcade.Sprite.draw(new_sprite)
