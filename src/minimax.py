from copy import deepcopy
import random

import evaluate
from legal_moves_list import all_legal_moves

openings = []

with open('src/openings/e4_openings.txt', 'r') as e4_openings:
    for line in e4_openings.readlines():
        l = line.strip().split(' ')
        openings.append(l)

with open('src/openings/d4_openings.txt', 'r') as d4_openings:
    for line in d4_openings.readlines():
        l = line.strip().split(' ')
        openings.append(l)

def minimax(current_board, who_to_move, alpha, beta, depth):

    if all_legal_moves(current_board, who_to_move) == []: 
        return (0, None)
    
    if depth == 0:
        return (evaluate.evaluate(current_board), None)

    # Removes irrelevant openings (of positions that have not occured in this game)
    for idx, move in enumerate(current_board.moves):
        for opening in openings:
            if len(opening) < current_board.ply:
                openings.remove(opening)
            if opening[idx] != move:
                openings.remove(opening)

    # if there are still relevant openings, play one of the moves
    if openings != []:
        return (None, openings[random.randint(0, len(openings)) - 1][current_board.ply])

    if who_to_move == 1:
        evaluation = (-999, None)

        for move in all_legal_moves(current_board, who_to_move):
            new_board = deepcopy(current_board)
            new_board.move(move)
            
            minimax_result = minimax(new_board, not who_to_move, alpha, beta, depth - 1)
            evaluation = evaluation if evaluation[0] >= minimax_result[0] else (minimax_result[0], move)

            if evaluation[0] >= beta[0]:
                break

            alpha = alpha if alpha[0] >= evaluation[0] else evaluation

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
                break

            beta = beta if beta[0] <= evaluation[0] else evaluation

        return evaluation
