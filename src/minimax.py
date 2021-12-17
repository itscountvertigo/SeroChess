from copy import deepcopy
import random

import evaluate
from legal_moves_list import all_legal_moves

from parse_openings import parse_openings
openings = parse_openings()

def minimax(current_board, who_to_move, alpha, beta, depth):
    legal_moves_list = all_legal_moves(current_board, who_to_move)

    if depth == 0:
        return (evaluate.evaluate(current_board), None)

    global openings

    if openings != [] and current_board.moves != []:
        new_openings = []
        for opening in openings:
            broken_off = False
            if len(opening) <= current_board.ply:
                continue
            for ply, move in enumerate(current_board.moves):
                if opening[ply] != move:
                    broken_off = True
                    break
            if not broken_off:
                new_openings.append(opening)

        openings = new_openings 

    # if there are still relevant openings, play one of the moves
    if openings != []:
        random_opening = openings[random.randint(0, len(openings) - 1)]
        print(f"move from opening: {random_opening}")
        return (None, random_opening[current_board.ply])

    if who_to_move == 1:
        evaluation = (-999, None)

        for move in legal_moves_list:
            new_board = deepcopy(current_board)
            new_board.move(move)
            
            minimax_result = minimax(new_board, not who_to_move, alpha, beta, depth - 1)
            evaluation = evaluation if evaluation[0] >= minimax_result[0] else (minimax_result[0], move)

            if evaluation[0] >= beta[0]:
                break

            alpha = alpha if alpha[0] >= evaluation[0] else evaluation

        has_king_w = False

        for piece in current_board.pieces:
            if piece.__class__.__name__ == 'King':
                has_king_w = True
        
        if not has_king_w:
            return (-9999, "Black wins")

        return evaluation

    else:
        evaluation = (999, None)

        for move in legal_moves_list:
            new_board = deepcopy(current_board)
            new_board.move(move)

            minimax_result = minimax(new_board, not who_to_move, alpha, beta, depth - 1)
            evaluation = evaluation if evaluation[0] <= minimax_result[0] else (minimax_result[0], move)

            # evaluation = min(evaluation, minimax(new_board, not who_to_move, alpha, beta, depth - 1))

            if evaluation[0] <= alpha[0]:
                break

            beta = beta if beta[0] <= evaluation[0] else evaluation

        has_king_b = False

        for piece in current_board.pieces:
            if piece.__class__.__name__ == 'King':
                has_king_b = True
        
        if not has_king_b:
            return (9999, "White wins")

        return evaluation
