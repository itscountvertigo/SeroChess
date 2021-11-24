import arcade
import gui
import cli

def main(mode):
    if mode == 'gui':
        window = gui.GUI(800, 800, "PWS Chess Engine")
        arcade.run()
    elif mode == 'cli':
        cli.player_vs_computer()

if __name__ == "__main__":
    main('gui')