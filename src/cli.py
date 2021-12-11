import time

from minimax import minimax
import board
from legal_moves_list import all_legal_moves

def player_vs_computer(player_w, player_b, depth):
    while True:
        if (board.main_board.who_to_move == 1 and player_w == 'computer') or (board.main_board.who_to_move == 0 and player_b == 'computer'):
            start_time = time.perf_counter()
            computer_move = minimax(board.main_board, board.main_board.who_to_move, (-9999, None), (9999, None), depth)
            end_time = time.perf_counter()

            print(f"Computer: {computer_move[1]}, calculated in {end_time - start_time} seconds")
            board.main_board.move(computer_move[1])

        else:
            legal_move_found = False
            while legal_move_found == False:
                player_move = input_move(board.main_board.who_to_move)
                if player_move != None:
                    board.main_board.move(player_move)
                    legal_move_found = True

        print("\nPosition: \n" + pos_to_cli_board(board.main_board))
        
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

    board_visualisation = [[0] * 8 for _ in range(8)]

    for piece in board.pieces:
        char = unicode_pieces[f"{'black' if piece.color == 0 else 'white'} {piece.__class__.__name__.lower()}"]
        board_visualisation[piece.y][piece.x] = char

    final_text = ""
    for rank in reversed(board_visualisation):
        for square in rank:
            final_text += "  " if square == 0 else str(square) + " "
        final_text += "\n"

    return final_text