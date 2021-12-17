import time
import rich

from minimax import minimax
import board
from legal_moves_list import all_legal_moves

def player_vs_computer(player_w, player_b, depth):
    while True:
        if (board.main_board.who_to_move == 1 and player_w == 'computer') or (board.main_board.who_to_move == 0 and player_b == 'computer'):
            start_time = time.perf_counter()
            computer_move = minimax(board.main_board, board.main_board.who_to_move, (-9999, None), (9999, None), depth)
            end_time = time.perf_counter()

            print(f"Computer: {computer_move[1]}, calculated in {end_time - start_time} seconds. Evaluation = {computer_move[0]}")
            board.main_board.move(computer_move[1])

        else:
            legal_move_found = False
            while legal_move_found == False:
                player_move = input_move(board.main_board.who_to_move)
                if player_move != None:
                    board.main_board.move(player_move)
                    legal_move_found = True

        rich.print(f"\nPosition: \n{pos_to_cli_board(board.main_board)} \n")
        
        
def input_move(player):
    player_move = input("Player: ")
    for move in all_legal_moves(board.main_board, player):
        if move == player_move:
            return move

    print("That's not a legal move!")
    return None

def pos_to_cli_board(board):
    unicode_pieces = {
        "black rook": "♖",
        "black knight": "♘",
        "black bishop": "♗",
        "black king": "♔",
        "black queen": "♕",
        "black pawn": "♙",
        "white rook": "♜",
        "white knight": "♞",
        "white bishop": "♝",
        "white king": "♚",
        "white queen": "♛",
        "white pawn": "♟︎"
    }

    final_text = ""

    for y in reversed(range(8)):
        for x in range(8):
            bg_color = f"{'#f0d9b5' if (x + y) % 2 else '#b58863'}"
            broken_off = False
            for piece in board.pieces:
                if piece.x == x and piece.y == y:
                    char = unicode_pieces[f"white {piece.__class__.__name__.lower()}"]
                    piece_color = 'red' if piece.color == 1 else 'blue'
                    final_text += f"[{piece_color} on {bg_color}] {char} [/{piece_color} on {bg_color}]"
                    broken_off = True
                    break
            if not broken_off:
                final_text += f"[white on {bg_color}]   [/white on {bg_color}]"
        final_text += '\n'

    return final_text
