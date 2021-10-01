import arcade

from board import board as board

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

        self.who_to_move = 1

        self.selected_squares = []
        
        arcade.set_background_color(self.color_w)

    def on_draw(self):
        arcade.start_render()
        self.draw_squares(self.width / 8, self.height / 8)
        
        self.draw_sprites(board)

        for each in self.selected_squares:
            arcade.draw_circle_filled(each[0] * self.width / 8 + self.width / 16, 
                                          each[1] * self.width / 8 + self.width / 16, 
                                          self.width / 32,
                                          [0, 0, 0, 30])

    def on_mouse_press(self, x, y, button, modifiers):
        coords = coords_to_square(x, y, self.width)

        for each in board:
            if each.x == coords[0] and each.y == coords[1] and self.who_to_move == each.color:
                legal_moves = each.legal_moves(board)

                if not each.selecting_squares:
                    self.selected_squares = []
                    for i in board:
                        i.selecting_squares = False

                    for i in legal_moves:
                        self.selected_squares.append(i)
                    each.selecting_squares = True
                else:
                    self.selected_squares = []
                    for i in board:
                        i.selecting_squares = False

            else:
                for square in self.selected_squares:
                    if coords[0] == square[0] and coords[1] == square[1] and each.selecting_squares:
                        each.move(square[0], square[1], board)
                        occupied = each.check_occupied(coords[0], coords[1], board)
                        if occupied == 1:
                            for i in board:
                                if coords[0] == i.x and coords[1] == i.y:
                                    board.remove(i)

                        self.who_to_move = not self.who_to_move
                        
                        self.selected_squares = []
                        for i in board:
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
