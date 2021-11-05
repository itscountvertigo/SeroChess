import arcade
import gui
from fen_import import read_FEN

def main():
    window = gui.GUI(800, 800, "PWS Chess Engine")
    arcade.run()

if __name__ == "__main__":
    main()