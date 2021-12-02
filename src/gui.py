import arcade

import board
# import check
from minimax import minimax
# from cli import pos_to_cli_board

from coords_to_square import coords_to_square

from evaluate import evaluate
import move_coords

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
        self.legal_moves = []
        
        arcade.set_background_color(self.color_w)

    def on_draw(self):
        arcade.start_render()
        self.draw_squares(self.width / 8, self.height / 8)
        
        self.draw_sprites(board.main_board.pieces)

        # draw circles on the legal moves of a selected piece
        for each in self.selected_squares:
            arcade.draw_circle_filled(
                each[0] * self.width / 8 + self.width / 16, 
                each[1] * self.width / 8 + self.width / 16, 
                self.width / 32,
                [0, 0, 0, 30]
            )

    def on_mouse_press(self, x, y, button, modifiers):
        coords = coords_to_square(x, y, self.width)
        
        print(board.main_board.check_square_occupied(coords[0], coords[1], board.main_board.who_to_move))

        # print(minimax.minimax(board.main_board, board.main_board.who_to_move, depth=1))

        for piece in board.main_board.pieces:
            # if clicked square has a piece:
            if piece.x == coords[0] and piece.y == coords[1] and board.main_board.who_to_move == piece.color:
                self.legal_moves = piece.legal_moves(board.main_board)
                print(self.legal_moves)

                legal_squares = []
                for move in self.legal_moves:
                    if move == "SHORT_CASTLE" or move == "LONG_CASTLE":
                        continue
                    legal_squares.append(move_coords.move_to_coords(move)[1])

                # if the piece is not selected, remove others' and highlight this one's
                if not piece.selecting_squares:
                    self.selected_squares = []
                    for i in board.main_board.pieces:
                        i.selecting_squares = False
                    """
                    if piece.__class__.__name__ == "King":
                        if piece.short_castle_allowed(board.main_board):
                            self.selected_squares.append([6,0] if piece.color == 1 else [6,7])
                        if piece.long_castle_allowed(board.main_board):
                            self.selected_squares.append([2,0] if piece.color == 1 else [2,7])
                    """

                    for i in legal_squares:
                        self.selected_squares.append(i)
                    piece.selecting_squares = True

                # if the piece is selected, unselect it (by emptying the selected squares array)
                else:
                    self.selected_squares = []
                    for i in board.main_board.pieces:
                        i.selecting_squares = False
            else:
                # if clicked square is one of a piece's selected and legal moves
                for square in self.selected_squares:
                    if coords[0] == square[0] and coords[1] == square[1] and piece.selecting_squares:
                        occupied = board.main_board.check_square_occupied(coords[0], coords[1], board.main_board.who_to_move)

                        # formatted_move_notation = generate_move_text.standard_notation(piece.x, piece.y, coords[0], coords[1], piece, occupied)
                        formatted_move = move_coords.coords_to_move(piece.x, piece.y, coords[0], coords[1])
                        """
                        if piece.__class__.__name__ == "King":
                            if piece.short_castle_allowed(board.main_board) and square[0] == 6 and square[1] == 0 if (piece.color == 1) else 7:
                                formatted_move = "SHORT_CASTLE"
                            elif piece.long_castle_allowed(board.main_board) and square[0] == 2 and square[1] == 0 if (piece.color == 1) else 7:
                                formatted_move = "LONG_CASTLE"
                        """

                        board.main_board.move(formatted_move)
                        board.main_board.moves.append(formatted_move)
                        
                        piece_type = piece.__class__.__name__
                        
                        # making in_starting_position (check for en passant / castling) false
                        if piece_type == "Pawn" or piece_type == "King" or piece_type == "Rook":
                            piece.in_starting_position = False

                            # en passant capturing
                            if piece_type == 'Pawn':
                                for i in board.main_board.pieces:
                                    if i == piece.enemy_en_passant_left:
                                        board.main_board.pieces.remove(i)
                                    elif i == piece.enemy_en_passant_right:
                                        board.main_board.pieces.remove(i)

                        print(evaluate(board.main_board))
                        
                        self.selected_squares = []
                        for i in board.main_board.pieces:
                            i.selecting_squares = False
    
        # print(pos_to_cli_board(board.main_board))

    def draw_squares(self, square_width, square_height):
        for x in range(8):
            for y in range(8):
                if x % 2 != y % 2:
                    arcade.draw_rectangle_filled(
                        x * square_width + square_width / 2, 
                        y * square_height + square_height / 2, 
                        square_width, 
                        square_height, 
                        self.color_b
                    )
    
    def draw_sprites(self, pieces):
        for each in pieces:
            new_sprite = arcade.Sprite(
                each.sprite_path,
                scale=1.2,
                center_x=(each.x * self.width / 8 + self.width / 16), 
                center_y=(each.y * self.height / 8 + self.width / 16)
            )
            arcade.Sprite.draw(new_sprite)
