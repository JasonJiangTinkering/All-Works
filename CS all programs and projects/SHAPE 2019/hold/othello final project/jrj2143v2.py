#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
An AI player for Othello. This is the template file that you need to  
complete and submit for the competition. 

@author: Jason Jiang
"""

import random
import sys
import time
 
# You can use the functions in othello_shared to write your AI 
from othello_shared import find_lines, get_possible_moves, get_score, play_move

def compute_utility(board, color):
    score = get_score(board)
    final = 2*(score[0] - score[1])
    
    
    
    if color == 1:
        anti = 2
    else:
        anti = 1

    for item in board[0]:#row one edge
        if item == color:
            final += 7
        elif item == anti:
            final -= 9
            
        else:
            continue
    for item in range(len(board)):
        if board[item][0] == color:
            final += 7
        elif board[item][0] == anti:
            final -= 9
        else:
            continue
        
    for item in range(len(board)):
        if board[item][-1] == color:
            final += 7
        elif board[item][-1] == anti:
            final -= 9
        else:
            continue
    for item in board[-1]:
        if item == color:
            final += 7
        elif item == anti:
            final -= 9
        else:
            continue
    
#        
#        
    
    
    
    return final
    #work on heristic
############ MINIMAX ##########################################################

def minimax_min_node(board, color):
    if color == 1:
        p = 1
    else:
        p = 2
      
    best = ( (-1, -1), 999)
    y = get_possible_moves(board, color)
    if len(y) == 0:
        return ((-1,-1), compute_utility(board, p ))

    for x in y:
        o = minimax_max_node(play_move(board, p, x[0], x[1]), p)
        if o[1] < best[1]:
            best = (x , o[1])
    return best


def minimax_max_node(board, color):
    best = ((-1, -1), -999)
    y = get_possible_moves(board, color)
    if len(y) == 0:
        return ((-1,-1), compute_utility(board, color))

    for x in y:
        o = minimax_min_node(play_move(board, color ,x[0], x[1]), color)
        if o[1] > best[1]:
            best = (x , o[1])
    return best

    
def select_move_minimax(board, color):#main
    """
    Given a board and a player color, decide on a move. 
    The return value is a tuple of integers (i,j), where
    i is the column and j is the row on the board.  
    """
    move, score = minimax_max_node(board, color)
    
    return move
        
#
#    
############ ALPHA-BETA PRUNING ########################################

#alphabeta_min_node(board, color, alpha, beta, level, limit)
def alphabeta_min_node(board, color, alpha, beta, start, allow, level, limit): 
    beta1 = beta
    if color == 1:
        r = 1
    else:
        r = 2
    y = get_possible_moves(board, r)
    now = time.time()
    if (len(y) == 0) or ((now - start) > allow) or (level > limit):
        return ((-1,-1), compute_utility(board, color))
    
    best = (y[0], 999)


    for x in y:
        if alpha > beta1:
            return x, -999
        q = alphabeta_max_node(play_move(board, color, x[0], x[1]), r, alpha, beta1, start, allow, level+1, limit)
        if q[1] < beta1:
            beta1 = q[1] 
        if q[1] < best[1]:
            best = x, q[1]
            
    return best
        


#alphabeta_max_node(board, color, alpha, beta, level, limit)
def alphabeta_max_node(board, color, alpha, beta, start, allow, level, limit):
    alpha1 = alpha
    y = get_possible_moves(board, color)
    now = time.time()
    if (len(y) == 0) or ((now - start) > allow) or (level > limit):
        return ((-1,-1), compute_utility(board, color))
    best = (y[0], -999)


    for x in y:
        if alpha1 > beta:
            return x, 999
        q = alphabeta_min_node(play_move(board, color, x[0], x[1]), color, alpha1, beta, start, allow, level+1, limit)
        if q[1] > alpha1:
            alpha1 = q[1]
        if q[1] > best[1]:
            best = x, q[1]
            
    return best#this returns the best possible move for us in the future 
        
            
        
        


def select_move_alphabeta(board, color): 
#return tuple (move, score)
    move,score = alphabeta_max_node(board, color, -999, 999, time.time(), 4, 0, 17)#worth
    
    return(move) #this returns the final best move
    

#################################################################
def run_ai():
    """
    This function establishes communication with the game manager. 
    It first introduces itself and receives its color. 
    Then it repeatedly receives the current score and current board state
    until the game is over. 
    """
    print("Jason") # First line is the name of this AI  
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
