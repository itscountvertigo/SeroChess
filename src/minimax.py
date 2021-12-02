import evaluate
import board
import legal_moves_list

from copy import deepcopy

def minimax(current_board, who_to_move, depth):
    if depth == 0:
        # print(evaluate.evaluate(current_board))
        return (evaluate.evaluate(current_board), None)

    max_evaluation = (-999, None) if who_to_move == 1 else (999, None)

    for move in legal_moves_list.all_legal_moves(current_board, who_to_move):
        new_board = deepcopy(current_board)
        new_board.move(move)
        new_evaluation = minimax(new_board, not who_to_move, depth - 1)

        print(new_evaluation, max_evaluation)

        if (who_to_move == 1 and new_evaluation[0] > max_evaluation[0]) or (who_to_move == 0 and new_evaluation[0] < max_evaluation[0]):
            best_move = move

        max_evaluation = (max(max_evaluation[0], new_evaluation[0]), 0) if who_to_move == 1 else (min(max_evaluation[0], new_evaluation[0]), 0)
    
    return (max_evaluation[0], best_move)