import evaluate
from legal_moves_list import all_legal_moves

from copy import deepcopy

def minimax(current_board, who_to_move, alpha, beta, depth):
    if all_legal_moves(current_board, who_to_move) == []: return (0, None)
    if depth == 0 or all_legal_moves(current_board, who_to_move) == []:
        # print(evaluate.evaluate(current_board))
        return (evaluate.evaluate(current_board), None)

    if who_to_move == 1:
        evaluation = (-999, None)

        for move in all_legal_moves(current_board, who_to_move):
            new_board = deepcopy(current_board)
            new_board.move(move)
            
            minimax_result = minimax(new_board, not who_to_move, alpha, beta, depth - 1)
            evaluation = evaluation if evaluation[0] >= minimax_result[0] else (minimax_result[0], move)

            if evaluation[0] >= beta[0]:
                print(f"BREAK! eval={evaluation}, beta={beta}, white to move")
                break

            alpha = alpha if alpha[0] >= evaluation[0] else evaluation

        print(f"depth={depth}, eval={evaluation}")

        return evaluation

    else:
        evaluation = (999, None)

        for move in all_legal_moves(current_board, who_to_move):
            new_board = deepcopy(current_board)
            new_board.move(move)

            minimax_result = minimax(new_board, not who_to_move, alpha, beta, depth - 1)
            evaluation = evaluation if evaluation[0] <= minimax_result[0] else (minimax_result[0], move)

            # evaluation = min(evaluation, minimax(new_board, not who_to_move, alpha, beta, depth - 1))

            if evaluation[0] <= alpha[0]:
                print(f"BREAK! eval={evaluation}, alpha={alpha}, black to move")
                break

            beta = beta if beta[0] <= evaluation[0] else evaluation

        return evaluation

"""
    max_evaluation = (-999, None) if who_to_move == 1 else (999, None)

    for move in legal_moves_list.all_legal_moves(current_board, who_to_move):
        new_board = deepcopy(current_board)
        new_board.move(move)
        new_evaluation = minimax(new_board, not who_to_move, depth - 1)

        if (who_to_move == 1 and new_evaluation[0] > max_evaluation[0]) or (who_to_move == 0 and new_evaluation[0] < max_evaluation[0]):
            best_move = move

        max_evaluation = (max(max_evaluation[0], new_evaluation[0]), 0) if who_to_move == 1 else (min(max_evaluation[0], new_evaluation[0]), 0)
    
    return (max_evaluation[0], best_move)
"""