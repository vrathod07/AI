""" Solving the 8 puzzel problem"""
import queue
import numpy as np

def board():
    initial_state = [[0,1,3],
                     [4,2,5],
                     [7,8,6]]
    final_state = [[1,2,3],
                   [4,5,6],
                   [7,8,0]]
    return initial_state,final_state

def get_index(matrix,value):
    for i, j in enumerate(matrix):
        for k, l in enumerate(j):
            if l == value:
                return i,k


class Problem:
    def __init__(self,initial,final):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal. Your subclass's constructor can add
        other arguments."""

        self.initial = initial
        self.goal = final


    def result(state,action):
        (row,col) = get_index(state,0)
        new_state = list(map(list, state))

        if action == "left":
            if col < len(new_state[0])-1:
                temp = new_state[row][col+1]
                new_state[row][col] = temp
                new_state[row][col+1] = 0
                return  new_state
            else:
                return
        if action == "right":
            if col != 0:
                temp = new_state[row][col - 1]
                new_state[row][col] = temp
                new_state[row][col - 1] = 0
                return new_state
            else:
                return

        if action == "up":
            if row < len(new_state[1])-1:
                temp = new_state[row+1][col]
                new_state[row][col] = temp
                new_state[row+1][col] = 0
                return new_state

            else:
                return

        if action == "down":
            if row != 0:
                temp = new_state[row-1][col]
                new_state[row][col] = temp
                new_state[row-1][col] = 0
                return new_state
            else:
                return

    def action(state):
        """The function takes current state and action to be performed as a parameter and returns
        a list of possible state reachable fom the current state after doing the particular action"""
        new_state = []
        all_state = []
        new_state = Problem.result(state,"left")
        if new_state != None:
            all_state.append(new_state)
        new_state = Problem.result(state,"right")
        if new_state != None:
            all_state.append(new_state)
        new_state = Problem.result(state,"up")
        if new_state != None:
            all_state.append(new_state)
        new_state = Problem.result(state,"down")
        if new_state != None:
            all_state.append(new_state)
        return all_state

    def goal_test(self,state):
        if self.goal == state:
            return True
        else:
            return False

    def path_cost(self,c,state1,action,state2):
        return c+1


class Node:
    def __init__(self,state,cost,move):
        self.state = state
        self.move = move
        self.cost = cost

    def expand(self):
        state = self.state
        next_states = Problem.action(state)
        nodes = []
        for state in next_states:
            nodes.append(Node(state,self.cost+1,self.move+1))
        return nodes



def solve(initial_state,goal_state):

    queue = []
    seq = []
    problem = Problem(initial_state, goal_state)

    while True:
       node = Node(initial_state, 0, 0)
       queue.append(node)
       next_nodes = node.expand()
       for node in next_nodes:
            queue.append(node)
       popped_node = queue.pop(0)
       if Problem.goal_test(popped_node.state):
            break




initial,goal = board()
solve(initial_state=initial,goal_state=goal)




