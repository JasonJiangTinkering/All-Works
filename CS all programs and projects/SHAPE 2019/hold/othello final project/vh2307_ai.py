#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
An AI player for Othello. This is the template file that you need to  
complete and submit for the competition. 

@author: Vivian Huynh
"""

import random
import sys
import time

# You can use the functions in othello_shared to write your AI 
from othello_shared import find_lines, get_possible_moves, get_score, play_move


############ MINIMAX ###############################

def minimax_min_node(board, color, level, limit):
    moves = get_possible_moves(board, color) #get all the possible moves
    if len(moves) == 0 or (level == limit): #if there are no more possible moves
        return (-1,-1), compute_utility(board, color) #return the current utility of the board
    min_move = None #the current best move
    min_score = float("inf") #the score of the best move
    other_color = 1 if color == 2 else 2 
    for move in moves: #for each possible move
        test = play_move(board, other_color, move[0], move[1]) #copy of the current board
        new_score = minimax_max_node(test, color, level + 1, limit)[1] #calculate the score of the board of the move was played
        if new_score < min_score: 
            min_score = new_score
            min_move = move
    return min_move, min_score

def minimax_max_node(board, color, level, limit):
    moves = get_possible_moves(board, color)
    if len(moves) == 0 or (level == limit):
        return (-1,-1), compute_utility(board, color)
    max_move = None
    max_score = float("-inf")
    for move in moves:
        test = play_move(board, color, move[0], move[1])
        new_score = minimax_min_node(test, color, level + 1, limit)[1]
        if new_score > max_score:
            max_score = new_score
            max_move = move
    return max_move, max_score

    
def select_move_minimax(board, color):
    """
    Given a board and a player color, decide on a move. 
    The return value is a tuple of integers (i,j), where
    i is the column and j is the row on the board.  
    """
    move, score = minimax_max_node(board, color, 0, 3)
    return move
    
############ ALPHA-BETA PRUNING #####################

#alphabeta_min_node(board, color, alpha, beta, level, limit)
def alphabeta_min_node(board, color, alpha, beta, timer, limit): 
    moves = get_possible_moves(board, color)
    if len(moves) == 0 or (time.monotonic() - timer > limit): #if there no more possible moves
        return (-1,-1), compute_utility(board, color) #return the score of that board
    min_move = moves[0]
    min_score = float("inf")
    current_move = 0 #move index
    b = beta
    other_color = 1 if color == 2 else 2 
    while (alpha < b) and (current_move < len(moves)):
        move = moves[current_move]
        test = play_move(board, other_color, move[0], move[1])
        new_score = alphabeta_max_node(test, color, alpha, b, timer, limit)[1]
        if new_score < min_score:
            min_score = new_score
            min_move = move
        if new_score < b:
            b = new_score
        current_move = current_move + 1
    return min_move, min_score


#alphabeta_max_node(board, color, alpha, beta, level, limit)
def alphabeta_max_node(board, color, alpha, beta, timer, limit):
    moves = get_possible_moves(board, color)
    if len(moves) == 0 or (time.monotonic() - timer > limit): #if there no more possible moves
        return (-1,-1), compute_utility(board, color) 
    max_move = moves[0]
    max_score = float("-inf")
    current_move = 0
    a = alpha
    while (a < beta) and (current_move < len(moves)):
        move = moves[current_move]
        test = play_move(board, color, move[0], move[1])
        new_score = alphabeta_min_node(test, color, a, beta, timer, limit)[1]
        if new_score > max_score:
            max_score = new_score
            max_move = move
        if new_score > a:
            a = new_score
        current_move = current_move + 1
    return max_move, max_score


def select_move_alphabeta(board, color): 
    move, score = alphabeta_max_node(board, color, float("-inf"), float("inf"), time.monotonic(), 5)
    return move

def compute_utility(board, color):
    score = get_score(board)
    dark = score[0]
    light = score[1]
    utility = dark - light
    other_color = 1 if color == 2 else 2 
    corners = [(0,0),(0,-1),(-1,0),(-1,-1)]
    for i in range(1,len(board)):
        #(0,i), (i,0), (-1,i), (i, -1)
        if board[0][i] == color:
            utility = utility + 2
        if board[i][0] == color:
            utility = utility + 2
        if board[-1][i] == color:
            utility = utility + 2
        if board[i][-1] == color:
            utility = utility + 2
        if board[0][i] == other_color:
            utility = utility - 3
        if board[i][0] == other_color:
            utility = utility - 3
        if board[-1][i] == other_color:
            utility = utility - 3
        if board[i][-1] == other_color:
            utility = utility - 3
    for corner in corners:
        if board[corner[0]][corner[1]] == color:
            utility = utility * 3
        elif board[corner[0]][corner[1]] == other_color:
            utility = utility * 0.1
    return utility
####################################################
def run_ai():
    """
    This function establishes communication with the game manager. 
    It first introduces itself and receives its color. 
    Then it repeatedly receives the current score and current board state
    until the game is over. 
    """
    print("Vivian") # First line is the name of this AI  
    color = int(input()) # Then we read the color: 1 for dark (goes first), 
                         # 2 for light. 

    while True: # This is the main loop 
        # Read in the current game status, for example:
        # "SCORE 2 2" or "FINAL 33 31" if the game is over.
        # The first number is the score for player 1 (dark), the second for player 2 (light)
        next_input = input() 
        status, dark_score_s, light_score_s = next_input.strip().split()
        dark_score = int(dark_score_s)
        light_score = int(light_score_s)

        if status == "FINAL": # Game is over. 
            print 
        else: 
            board = eval(input()) # Read in the input and turn it into a Python
                                  # object. The format is a list of rows. The 
                                  # squares in each row are represented by 
                                  # 0 : empty square
                                  # 1 : dark disk (player 1)
                                  # 2 : light disk (player 2)
                    
            # Select the move and send it to the manager 
#            movei, movej = select_move_minimax(board, color)
            movei, movej = select_move_alphabeta(board, color)
            print("{} {}".format(movei, movej)) 


if __name__ == "__main__":
    run_ai()
