import evaluate
import board
import legal_moves_list

import copy

def minimax(current_board, who_to_move, depth):
    if depth == 0:
        return evaluate.evaluate(current_board)

    max_evaluation = 999 if who_to_move == 1 else -999

    for move in legal_moves_list.all_legal_moves(current_board, who_to_move):
        new_board = board.Board(current_board.pieces, who_to_move, 1, 0, [])
        new_board.move(move)
        new_evaluation = minimax(new_board, not who_to_move, depth - 1)

        max_evaluation = max(max_evaluation, new_evaluation) if who_to_move == 1 else min(max_evaluation, new_evaluation)
    
    return max_evaluation