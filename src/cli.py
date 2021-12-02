from minimax import minimax
import random
import board
from legal_moves_list import all_legal_moves

def player_vs_computer(player=1):
    while True:
        # if computers move, find best move
        if board.main_board.who_to_move != player:
            # find best legal moves (call to minimax giving current pos)
            
            """
            legal_moves = all_legal_moves(board.main_board, not player)
            computer_move = legal_moves[random.randint(0, len(legal_moves) - 1)]
            print("Computer: " + computer_move)
            board.main_board.move(computer_move)
            """

            computer_move = minimax(board.main_board, board.main_board.who_to_move, depth=2)
            print("Computer: " + computer_move[1])
            board.main_board.move(computer_move[1])

        # if players move, await input and process it
        else:
            legal_move_found = False
            while legal_move_found == False:
                player_move = input_move(player)
                if player_move != None:
                    board.main_board.move(player_move)
                    legal_move_found = True

        # print("Minimax Eval: " + str(minimax.minimax(board.main_board, board.main_board.who_to_move, depth=2)) + "\n")

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