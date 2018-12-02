# pacmanAgents.py
# ---------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from pacman import Directions
from game import Agent
from heuristics import scoreEvaluation
import random



class RandomAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # get all legal actions for pacman
        actions = state.getLegalPacmanActions()
        # returns random action from all the valide actions
        print actions[random.randint(0,len(actions)-1)]
        return actions[random.randint(0,len(actions)-1)]

class GreedyAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # get all legal actions for pacman
        legal = state.getLegalPacmanActions()

        # get all the successor state for these actions
        successors = [(state.generateSuccessor(0, action), action) for action in legal]
        for ele in successors:
            print "ele =", ele


        # evaluate the successor states using scoreEvaluation heuristic
        scored = [(scoreEvaluation(state), action) for state, action in successors]
        # get best choice
        bestScore = max(scored)[0]
        # get all actions that lead to the highest score
        bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
        print bestActions
        # return random action from the list of the best actions
        return random.choice(bestActions)

class BFSAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write BFS Algorithm instead of returning Directions.STOP

        fringe = Queue()                                        # instance of Queue class
        legal = state.getLegalPacmanActions()
        bestScore=[]                                            # to store the node with the maximum score and the associated action
        score = []                                              # list storing the score for all the fringe nodes
        terminal=[]                                             # to store state leading to none state
        winState=[]                                             # store all the win states

        for actions in legal:
            ns = state.generatePacmanSuccessor(actions)
            fringe.push((ns,actions))                           # Initial states pushed on to the queue

        while not fringe.isEmpty():
                                                                # Loop runs unitl queue has nodes
            newState,action = fringe.pop()                      # pop the nodes in FIFO manner
            if newState.isWin():
                winState.append((newState,action))              # if the state is a win state, append it to the winState list
            elif newState.isLose():
                continue                                        # if the state is a lose state, continue
            else:
                legal1 = newState.getLegalPacmanActions()       # else explore paths for all other nodes
                for ele in legal1:
                    ns1 = newState.generatePacmanSuccessor(ele)

                    if ns1 != None:
                        fringe.push((ns1,action))               #if the state doesn't reutrn None, push it to the Stack
                    else:
                        terminal.append((newState,action))      #if the state returns None, add it to the terminal

        if len(winState) != 0:                                  #if winState has elements, append the scores for all win states to 'score' list
            for state,action in winState:
                score.append((scoreEvaluation(state),action))

        else:                                                   #if winState has no elements, append the scores for all win states to 'score' list
            for state,action in terminal:
                score.append((scoreEvaluation(state), action))

        bestScore = max(score, key=lambda x: x[0])              #calculating and storing the highest score node and the associated action in bestScore
        return bestScore[1]                                     #return the direction


class DFSAgent(Agent):

    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write DFS Algorithm instead of returning Directions.STOP

        fringe = Stack()                                        # instance of Stack class

        bestScore = []                                           # to store the node with the maximum score and the associated action
        score = []                                               # list storing the score for all the fringe nodes
        terminal = []                                            # to store state leading to none state
        winState = []                                            # store all the win states

        legal = state.getLegalPacmanActions()

        for actions in legal:
            ns = state.generatePacmanSuccessor(actions)
            fringe.push((ns, actions))                           # Initial states pushed on to the queue

        while not fringe.isEmpty():
                                                                # Loop runs unitl Stack has nodes
            newState,action = fringe.pop()                      # pop the nodes in FIFO manner
            if newState.isWin():
                winState.append((newState,action))              # if the state is a win state, append it to the winState list
            elif newState.isLose():
                continue                                        # if the state is a lose state, continue
            else:
                legal1 = newState.getLegalPacmanActions()       # else explore paths for all other nodes
                for ele in legal1:
                    ns1 = newState.generatePacmanSuccessor(ele)

                    if ns1 != None:
                        fringe.push((ns1,action))               #if the state doesn't reutrn None, push it to the Stack
                    else:
                        terminal.append((newState,action))      #if the state returns None, add it to the terminal

        if len(winState) != 0:                                  #if winState has elements, append the scores for all win states to 'score' list
            for state,action in winState:
                score.append((scoreEvaluation(state),action))

        else:                                                   #if winState has no elements, append the scores for all win states to 'score' list
            for state,action in terminal:
                score.append((scoreEvaluation(state), action))

        bestScore = max(score, key=lambda x: x[0])              #calculating and storing the highest score node and the associated action in bestScore
        return bestScore[1]                                     #return the direction


class AStarAgent(Agent):
    # Initialization Function: Called one time when the game starts

    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write A* Algorithm instead of returning Directions.STOP

        fringe = Queue()                                        # instance of Queue class
        score = []                                              # list storing the score for all the fringe nodes
        bestScore = ()                                          # to store the node with the maximum score and the associated action
        depth = 1                                               # Initialising initial depth for the node that is 1
        winState=[]                                             # store all the win states
        terminal=[]                                             # to store state leading to none state

        legal = state.getLegalPacmanActions()

        for actions in legal:
            ns = state.generatePacmanSuccessor(actions)
            cost = depth - (scoreEvaluation(ns) - scoreEvaluation(state))       #Calculating the evaluation function for the initial states

            fringe.push((ns, actions,cost,depth))                               #push states on to the queue


        while not fringe.isEmpty():                                             #Loop until queue has elements


            fringe.getList().sort(key=lambda x:x[2])                            #sorting the queue in ascending order based on 'cost'
            fringe.getList().reverse()                                          #revrsing the list so that the node with the lowest cost is popped for exploration
            newState, action, c,d = fringe.pop()                                #pop the node in FIFO manner

            if newState.isWin():
                winState.append((newState,action))
            elif newState.isLose():
                continue
            else:
                legal1 = newState.getLegalPacmanActions()

                for ele in legal1:
                    ns1 = newState.generatePacmanSuccessor(ele)
                    if ns1 != None:
                        cost = (d+1) - (scoreEvaluation(ns1) - scoreEvaluation(state))          #calculate the cost(evaluation function) of the nodes and push on to the queue
                        fringe.push((ns1, action,cost,(d+1)))

                    else:
                        terminal.append((newState,action))                                      #if node returns none for the next successor, append it to the 'terminal' list




        if len(winState)!= 0:                                                       #if winState has nodes, append it to the 'score' list
            for state,action in winState:
                score.append((scoreEvaluation(state), action))
        else:                                                                       #else calculate score for other nodes and and append it to 'score' list
            for state,action in terminal:
                score.append((scoreEvaluation(state), action))

        bestScore = max(score, key=lambda x: x[0])                                  #calculate the highest score among all the nodes
        return bestScore[1]                                                         #return the direction

"""
class AStarAgent(Agent):
    # Initialization Function: Called one time when the game starts

    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write A* Algorithm instead of returning Directions.STOP

        fringe = Queue()
        legal = state.getLegalPacmanActions()
        score = []
        bestScore = ()
        depth = 1
        bool = False

        for actions in legal:
            ns = state.generatePacmanSuccessor(actions)
            if ns.isWin():
                bool = True
                return actions

            cost = depth - (scoreEvaluation(ns) - scoreEvaluation(state))

            fringe.push((ns, actions,cost,depth))


        while not fringe.isEmpty():
            if bool == True:
                break

            fringe.getList().sort(key=lambda x:x[2])
            fringe.getList().reverse()

            newState, action, c,d = fringe.pop()

            if newState.isWin():
                return action
            if newState.isLose():
                continue
            legal1 = newState.getLegalPacmanActions()

            for ele in legal1:
                ns1 = newState.generatePacmanSuccessor(ele)
                if ns1 != None:
                    cost = (d+1) - (scoreEvaluation(ns1) - scoreEvaluation(state))
                    fringe.push((ns1, action,cost,(d+1)))

                else:
                    bool = True
                    break

        for ns,actions, cost,de in fringe.getList():
            score.append((scoreEvaluation(ns),actions,cost,de))

        bestScore = max(score, key=lambda x: x[0])
        return bestScore[1]


"""

class Stack:
    def __init__(self):
        self.list = []

    def push(self,element):
        "push element in stack"
        self.list.append(element)

    def pop(self):
        "pop element from the stack (LIFO)"
        return self.list.pop()

    def display(self):
        "display stack elements"
        i = 0
        for ele in self.list:
            print i, " ", ele," "
            i = i + 1

    def isEmpty(self):
        "check whether stack is empty or not"
        length = len(self.list)
        return length == 0

    def getList(self):
        return self.list



class Queue:
    def __init__(self):
        self.list = []

    def push(self,element):
        "push element in queue"
        self.list.insert(0,element)

    def pop(self):
        "pop element from the queue (FIFO)"
        return self.list.pop()

    def display(self):
        "display stack elements"
        print "in display"
        print self.getList()

    def isEmpty(self):
        "check whether queue is empty or not"
        length = len(self.list)
        return length == 0

    def getList(self):
        return self.list
