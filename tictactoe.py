"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount = 0
    oCount = 0
    for row in range(3):
        for col in range(3):
            if board[row][col] == X:
                xCount += 1
            elif board[row][col] == O:
                oCount += 1
    if xCount > oCount:
        return O
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    states = set()
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                states.add((row,col))
    return states


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # horizontal rows
    if all(i == board[0][0] for i in board[0]):
        return board[0][0]
    elif all(i == board[1][0] for i in board[1]):
        return board[1][0]
    elif all(i == board[2][0] for i in board[2]):
        return board[2][0]
    # vertical columns
    elif all(board[i][0] == board[0][0] for i in range(3)):
        return board[0][0]
    elif all(board[i][1] == board[0][1] for i in range(3)):
        return board[0][1]
    elif all(board[i][2] == board[0][2] for i in range(3)):
        return board[0][2]
    # diagonals
    elif(board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return board[0][0]
    elif(board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or (not any(EMPTY in row for row in board) and winner(board) is None):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    Max = float("-inf")
    Min = float("inf")

    if player(board) == X:
        return Max_Value(board, Max, Min)[1]
    else:
        return Min_Value(board, Max, Min)[1]

def Max_Value(board, Max, Min):
    move = None
    
    if terminal(board):
        return [utility(board), None]
    
    v = float('-inf')
    for action in actions(board):
        
        test = Min_Value(result(board, action), Max, Min)[0]
        Max = max(Max, test)
        
        if test > v:
            v = test
            move = action
        # Alphabeta pruning Optimisation
        if Max >= Min:
            break
    return [v, move]

def Min_Value(board, Max, Min):
    move = None
    
    if terminal(board):
        return [utility(board), None]
    
    v = float('inf')
    for action in actions(board):
        test = Max_Value(result(board, action), Max, Min)[0]
        Min = min(Min, test)
        if test < v:
            v = test
            move = action
        # Alphabeta pruning optimisation
        if Max >= Min:
            break
    return [v, move]