import Board
import time
from math import inf


time_start = time.time()

root = Board.Board([
    " ", " ", " ",
    " ", " ", " ",
    " ", " ", " "
])

node_counter = 0


def build_tree(board, is_player1):
    children = []

    if is_player1:
        for i in board.free_spaces():
            child = Board.Board(board.board.copy())
            child.board[i] = board.player1
            children.append(child)

    else:
        for i in board.free_spaces():
            child = Board.Board(board.board.copy())
            child.board[i] = board.player2
            children.append(child)

    board.children = children

    for i in children:
        if i.value is None:
            build_tree(i, not is_player1)


def min_value(board):
    if board.value is not None:
        return board.value

    min_eval = inf
    for i in board.children:
        eval = max_value(i)
        min_eval = min(min_eval, eval)
    return min_eval


def max_value(board):
    if board.value is not None:
        return board.value

    max_eval = -inf
    for i in board.children:
        eval = min_value(i)
        max_eval = max(max_eval, eval)
    return max_eval


def min_value_pruning(board, alpha, beta):
    if board.value is not None:
        return board.value

    min_eval = inf
    for i in board.children:
        eval = max_value_pruning(i, alpha, beta)
        min_eval = min(min_eval, eval)
        beta = min(beta, eval)
        if beta <= alpha:
            break
    return min_eval


def max_value_pruning(board, alpha, beta):
    if board.value is not None:
        return board.value

    max_eval = -inf
    for i in board.children:
        eval = min_value_pruning(i, alpha, beta)
        max_eval = max(max_eval, eval)
        alpha = max(alpha, eval)
        if beta <= alpha:
            break
    return max_eval


def minimax(board, is_maximizing):
    global node_counter
    node_counter += 1
    if board.value is not None:
        return board.value

    if is_maximizing:
        max_eval = -inf
        for i in board.children:
            eval = minimax(i, False)
            max_eval = max(max_eval, eval)
        return max_eval

    else:
        min_eval = inf
        for i in board.children:
            eval = minimax(i, True)
            min_eval = min(min_eval, eval)
        return min_eval


def minimax_pruning(board, is_maximizing, alpha, beta):
    global node_counter
    node_counter += 1
    if board.value is not None:
        return board.value

    if is_maximizing:
        max_eval = -inf
        for i in board.children:
            eval = minimax_pruning(i, False, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval

    else:
        min_eval = inf
        for i in board.children:
            eval = minimax_pruning(i, True, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval



build_tree(root, True)
root.print()
print(f"Finished building tree after {time.time() - time_start} seconds.")

max_value(root)
max_value_pruning(root, -inf, inf)


minimax_pruning(root, True, -inf, inf)
print(node_counter)

print("--------------------------------------------")
node_counter = 0

minimax(root, True)
print(node_counter)