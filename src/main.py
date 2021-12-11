import argparse
import arcade

import gui
import cli

def main(mode, player_w, player_b, depth):
    if mode == 'gui':
        window = gui.GUI(800, 800, "PWS Chess Engine")
        arcade.run()

    elif mode == 'cli':
        cli.player_vs_computer(player_w, player_b, depth)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument(dest="mode", type=str, help="Which mode to use, pick from 'cli' or 'gui'. If you are playing against a computer, please pick 'cli'.")
    parser.add_argument(dest="player_w", type=str, help="Who is player one? Pick from 'computer' or 'player'.")
    parser.add_argument(dest="player_b", type=str, help="Who is player one? Pick from 'computer' or 'player'.")
    parser.add_argument('-d', '--depth', type=int, help="Computer depth, only relevant if one of the players is a computer.")

    args = parser.parse_args()

    main(args.mode, args.player_w, args.player_b, args.depth)