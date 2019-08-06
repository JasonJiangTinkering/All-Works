# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 14:21:05 2019

@author: jrj2143
"""

"""
SHAPE'19

In this assignment you will implement and compare different search strategies
for solving the n-Puzzle, which is a generalization of the 8 and 15 puzzle to
squares of arbitrary size (we will only test it with 8-puzzles for now). 
See Courseworks for detailed instructions.

"""

import time

def state_to_string(state):
    row_strings = [" ".join([str(cell) for cell in row]) for row in state]
    x = "\n".join(row_strings)
    x = x.replace("0", " ")
    return x

def swap_cells(state, i1, j1, i2, j2):
    """
    Returns a new state with the cells (i1,j1) and (i2,j2) swapped. 
    """
    value1 = state[i1][j1]
    value2 = state[i2][j2]
    
    new_state = []
    for row in range(len(state)): 
        new_row = []
        for column in range(len(state[row])): 
            if row == i1 and column == j1: 
                new_row.append(value2)
            elif row == i2 and column == j2:
                new_row.append(value1)
            else: 
                new_row.append(state[row][column])
        new_state.append(tuple(new_row))
    return tuple(new_state)
    

def get_successors(state):
    """
    This function returns a list of possible successor states resulting
    from applicable actions. 
    The result should be a list containing (Action, state) tuples. 
    For example [("Up", ((1, 4, 2),(0, 5, 8),(3, 6, 7))), 
                 ("Left",((4, 0, 2),(1, 5, 8),(3, 6, 7)))] 
    """ 
    child_states = []

    for row in range(len(state)):
        for column in range(len(state[row])):
            if state[row][column] == 0:
                if column < len(state)-1: # Left 
                    new_state = swap_cells(state, row,column, row, column+1)
                    child_states.append(("Left",new_state))
                if column > 0: # Right 
                    new_state = swap_cells(state, row,column, row, column-1)
                    child_states.append(("Right",new_state))
                if row < len(state)-1:   #Up 
                    new_state = swap_cells(state, row,column, row+1, column)
                    child_states.append(("Up",new_state))
                if row > 0: # Down
                    new_state = swap_cells(state, row,column, row-1, column)
                    child_states.append(("Down", new_state))
                break
    return child_states

            
def goal_test(state):
    """
    Returns True if the state is a goal state, False otherwise. 
    """    
    counter = 0
    for row in state:
        for cell in row: 
            if counter != cell: 
                return False 
            counter += 1
    return True
def bfs(state):
    print(manhattan_heuristic(state))
    """
    Breadth first search.
    Returns three values: A list of actions, the number of states expanded, and
    the maximum size of the frontier.  
    """
    
    FIFO_queue = [state]
    parents = {}
    actions = {}
    costs = {}

    finalaction = []
    costs[state] = 0#1 - come to later
    stateexpand = 0#6^^
    hold = [] #hold the potential moves to see if in visited
    hold2 = []#hold one moves so we can target the tuple

    fronter = 0
##    FIFO_queue.extend(get_successors(state))#2
##    parents[state] = 'end'#3^^
##    actions[state] = 'end'#4^^
##    visited.append(state)#5 ^^
    print(state) 
    print(misplaced_heuristic(state))
    for item in FIFO_queue:
        
        stateexpand += 1#6
##        print(item)
##        print(type(item))

##        print(stateexpand)
        
        if goal_test(item) == True:
            untill = item
            while untill != state:
                finalaction.insert(0, actions[untill])
                untill = parents[untill]
                
            fronter = len(FIFO_queue) - FIFO_queue.index(item)
            return(finalaction, stateexpand, fronter)#**** is list of actions to get goal and 123 is the max size of fronter-> number of items after goal
            return('finished') #del later
        hold = get_successors(item)
        for y in hold:
            hold2 = y
            if hold2[1] not in parents:
##                print('new state:', hold2[1])
                actions[hold2[1]] = hold2[0]#4
                parents[hold2[1]] = item #3
                FIFO_queue.append(hold2[1])
##
#        if len(visited) >= math.factorial(9):
#            print('all variants found')
                
            
            
##    print(get_successors(state))
##    print(state_to_string(state))

    # Write code here for bfs.  
                
    return None# No solution found
                      
     
def dfs(state):
    """
    Depth first search.
    Returns three values: A list of actions, the number of states expanded, and
    the maximum size of the frontier.  
    """
#        -----------------
#    FIFO_queue = [state]
#    parents = {}
#    actions = {}
#    costs = {}
#
#    finalaction = []
#    costs[state] = 0#1 - come to later
#    stateexpand = 0#6^^
#    hold = [] #hold the potential moves to see if in visited
#    hold2 = []#hold one moves so we can target the tuple
#
#    fronter = 0
###    FIFO_queue.extend(get_successors(state))#2
###    parents[state] = 'end'#3^^
###    actions[state] = 'end'#4^^
###    visited.append(state)#5 ^^
#    
#    for item in FIFO_queue:
#
#        stateexpand += 1#6
##        print(item)
##        print(type(item))
##
##        print(stateexpand)
#        
#        if goal_test(item) == True:
#            untill = item
#            while untill != state:
#                finalaction.insert(0, actions[untill])
#                untill = parents[untill]
#                
#            fronter = len(FIFO_queue) - FIFO_queue.index(item)
#            return(finalaction, stateexpand, fronter)#**** is list of actions to get goal and 123 is the max size of fronter-> number of items after goal
#            return('finished') #del later
#        hold = get_successors(item)
#        for y in hold:
#            hold2 = y
#            if hold2[1] not in parents:
###                print('new state:', hold2[1])
#                actions[hold2[1]] = hold2[0]#4
#                parents[hold2[1]] = item #3
#                FIFO_queue.insert(FIFO_queue.index(item) +1 , hold2[1])
#   -----------------------


          
##
#        if len(visited) >= math.factorial(9):
#            print('all variants found')
                
            
            
##    print(get_successors(state))
##    print(state_to_string(state))

    # Write code here for bfs.  
                
    return None# No solution found


def misplaced_heuristic(state):
    """
    Returns the number of misplaced tiles.
    """
    
    goal = 0
    mis = 0

    for y in state:
        for x in y:
            if x != goal:
                mis += 1
#                print(2)
            goal += 1
#            print(1)
#    print(mis)
    return(mis)
            


def manhattan_heuristic(state):
    """
    For each misplaced tile, compute the manhattan distance between the current
    position and the goal position. THen sum all distances. 
    """
    goal = 0
    mis = 0

    for y in state:
        for x in y:
            mis+= (abs(goal - x) //3) + (abs(abs(goal - x) % 3))
            goal += 1
    
    return(mis) # replace this
    

def get_solution(state, parents, actions, costs):
    """
    Helper function to retrieve the solution. This was not part of the
    provided scaffolding.
    """
    
    # Write solution traversal here

    return []


def best_first(state, heuristic = misplaced_heuristic):
    """
    Breadth first search using the heuristic function passed as a parameter.
    Returns three values: A list of actions, the number of states expanded, and
    the maximum size of the frontier.  
    """

    # You might want to use these functions to maintain a priority queue
    # You may also use your own heap class here
    from heapq import heappush
    from heapq import heappop
    FIFO_queue = []
    parents = {}
    actions = {}
    costs = {}

    finalaction = []
    costs[state] = 0#1 - come to later
    stateexpand = 0#6^^
    hold = [] #hold the potential moves to see if in visited
    hold2 = []#hold one moves so we can target the tuple
    
    fronter = 0
##    FIFO_queue.extend(get_successors(state))#2
##    parents[state] = 'end'#3^^
##    actions[state] = 'end'#4^^
##    visited.append(state)#5 ^^
##    print('first:',state) 
    heappush(FIFO_queue, (heuristic(state), state))
    while True:
        item = heappop(FIFO_queue)
        stateexpand += 1#6
##        print(item)
##        print(type(item))

##        print(stateexpand)
##        print(item[1])
        if goal_test(item[1]) == True:
            untill = item[1]
            
            while untill != state:
                finalaction.insert(0, actions[untill])
##                print(finalaction)
                untill = parents[untill]
            fronter = len(FIFO_queue)
            print('how many states visited:', stateexpand, 'size of frontier:', fronter)
            print(finalaction)
            return(finalaction)

        hold = get_successors(item[1])
        for y in hold:
            hold2 = y
            if hold2[1] not in parents:
##                print('new state:', hold2[1])
                actions[hold2[1]] = hold2[0]#4
##                print('parent', item[1])
##                print('child', hold2[1])
                parents[hold2[1]] = item[1] #3
##                print('state', hold2)
                
                heappush(FIFO_queue,(heuristic(hold2[1]), hold2[1]))
##
#        if len(visited) >= math.factorial(9):
#            print('all variants found')
                
            
            
##    print(get_successors(state))
##    print(state_to_string(state))

    # Write code here for bfs.  
                
    return(None)# No solution found
                      


def astar(state, heuristic = misplaced_heuristic):
    """
    A-star search using the heuristic function passed as a parameter. 
    Returns three values: A list of actions, the number of states expanded, and
    the maximum size of the frontier.  
    """
    """
    Breadth first search using the heuristic function passed as a parameter.
    Returns three values: A list of actions, the number of states expanded, and
    the maximum size of the frontier.  
    """

    # You might want to use these functions to maintain a priority queue
    # You may also use your own heap class here
    from heapq import heappush
    from heapq import heappop
    FIFO_queue = []
    parents = {}
    actions = {}
    costs = {}

    finalaction = []
    costs[state] = 0#1 - come to later
    stateexpand = 0#6^^
    hold = [] #hold the potential moves to see if in visited
    hold2 = []#hold one moves so we can target the tuple
    
    fronter = 0
##    FIFO_queue.extend(get_successors(state))#2
##    parents[state] = 'end'#3^^
##    actions[state] = 'end'#4^^
##    visited.append(state)#5 ^^
##    print('first:',state) 
   
    heappush(FIFO_queue, (manhattan_heuristic(state), state))
    while True:
        
        item = heappop(FIFO_queue)
        stateexpand += 1#6
##        print(item)
##        print(type(item))

##        print(stateexpand)
#        print(item[1])
        if goal_test(item[1]) == True:
            untill = item[1]
            
            while untill != state:
                finalaction.insert(0, actions[untill])
##                print(finalaction)
                untill = parents[untill]
            fronter = len(FIFO_queue)
            print('how many states visited:', stateexpand, 'size of frontier:', fronter)
            print(finalaction)
            return(finalaction)
                
        hold = get_successors(item[1])
        for y in hold:
            hold2 = y
            if hold2[1] not in parents:
##                print('new state:', hold2[1])
                actions[hold2[1]] = hold2[0]#4
##                print('parent', item[1])
##                print('child', hold2[1])
                parents[hold2[1]] = item[1] #3
##                print('state', hold2)
#                print(manhattan_heuristic(hold2[1]))
#                print(layer)
                costs[hold2[1]] = costs[item[1]] +1
                heappush(FIFO_queue,(manhattan_heuristic(hold2[1]) + costs[hold2[1]], hold2[1]))
##
#        if len(visited) >= math.factorial(9):
#            print('all variants found')
                
            
            
##    print(get_successors(state))
##    print(state_to_string(state))

    # Write code here for bfs.  
                
    return(None)# No solution found
                      


def print_result(solution):
    """
    Helper function to format test output. 
    """
    if solution is None: 
        print("No solution found.")
    else: 
        print("Solution has {} actions.".format(len(solution)))



if __name__ == "__main__":

##    #Easy test case
##    test_state = ((1, 4, 2),
##                  (0, 5, 8),  
##                  (3, 6, 7))  

    #More difficult test case
    test_state = ((7, 2, 4),
                  (5, 0, 6), 
                  (8, 3, 1))  

    print(state_to_string(test_state))
    print()

    print("====BFS====")
    start = time.time()
    solution = bfs(test_state) #
    print_result(solution)
    end = time.time()
    if solution is not None:
        print(solution)
    print("Total time: {0:.3f}s".format(end-start))

    print() 
    print("====DFS====") 
    start = time.time()
    solution = dfs(test_state)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))


##    print() 
##    print("====Greedy DFS// best first====") 
##    start = time.time()
##    solution = best_first(test_state, misplaced_heuristic)
##    end = time.time()
##    print_result(solution)
##    print("Total time: {0:.3f}s".format(end-start))
##    

    print() 
    print("====Best-First====") 
    start = time.time()
    solution = best_first(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))
    
    print() 
    print("====A* (Misplaced Tiles Heuristic)====") 
    start = time.time()
    solution = astar(test_state, manhattan_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))

