import arcade

from pieces import king, queen, rook, knight, bishop, pawn

board = [king.King(4, 0, 1),                              # white king
         queen.Queen(3, 0, 1),                            # white queen
         bishop.Bishop(2, 0, 1), bishop.Bishop(5, 0, 1),  # white bishops
         knight.Knight(1, 0, 1), knight.Knight(6, 0, 1),  # white knights
         rook.Rook(0, 0, 1), rook.Rook(7, 0, 1),          # white rooks
         king.King(4, 7, 0),                              # black king
         queen.Queen(3, 7, 0),                            # black queen
         bishop.Bishop(2, 7, 0), bishop.Bishop(5, 7, 0),  # black bishops
         knight.Knight(1, 7, 0), knight.Knight(6, 7, 0),  # black knights
         rook.Rook(0, 7, 0), rook.Rook(7, 7, 0)           # black rooks
        ]

for i in range(8):
    board.append(pawn.Pawn(i, 1, 1))  # add white pawns
    board.append(pawn.Pawn(i, 6, 0))  # add black pawns

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
        
        arcade.set_background_color(self.color_w)

    def on_draw(self):
        arcade.start_render()
        self.draw_squares(self.width / 8, self.height / 8)
        
        sprites = self.create_sprites(board)

        for each in sprites:
            arcade.Sprite.draw(each)

    def draw_squares(self, square_width, square_height):
        for x in range(8):
            for y in range(8):
                if x % 2 != y % 2:
                    arcade.draw_rectangle_filled(x * square_width + square_width / 2, 
                                                 y * square_height + square_height / 2, 
                                                 square_width, 
                                                 square_height, 
                                                 self.color_b)
    
    def create_sprites(self, pieces):
        sprites = []

        for each in pieces:
            new_sprite = arcade.Sprite(each.sprite_path,
                                       scale=1.2,
                                       center_x=(each.x * self.width / 8 + self.width / 16), 
                                       center_y=(each.y * self.height / 8 + self.width / 16))
            sprites.append(new_sprite)

        return sprites

def main():
    window = GUI(800, 800, "PWS Chess Engine")
    arcade.run()

if __name__ == "__main__":
    main()