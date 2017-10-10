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
import Queue

class RandomAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # get all legal actions for pacman
        actions = state.getLegalPacmanActions()
        # returns random action from all the valide actions
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
        # evaluate the successor states using scoreEvaluation heuristic
        scored = [(scoreEvaluation(state), action) for state, action in successors]
        # get best choice
        bestScore = max(scored)[0]
        # get all actions that lead to the highest score
        bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
        # return random action from the list of the best actions
        return random.choice(bestActions)

class BFSAgent(Agent):

    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write BFS Algorithm instead of returning Directions.STOP
        legal = state.getLegalPacmanActions()
        successors = [(state.generateSuccessor(0, action), action) for action in legal]

        bestScore = []
        for state, action in successors:
            if state.isWin() or state.isLose():
                return action
            bestScore.append((BFSAgent.bfs(self, state), action))

        bfs_best = max(bestScore)[0]
        bfs_action = [pair[1] for pair in bestScore if pair[0] == bfs_best]

        return bfs_action[0]
        # if len(bfs_action) > 1:
        #     return random.choice(bfs_action)
        # else:
        #     return bfs_action[0]

    # Perform bfs on each state and return best score
    def bfs(self, state):
        legal = state.getLegalPacmanActions()
        successors = [(state.generateSuccessor(0, action), action) for action in legal]

        path = Queue.Queue()
        explored = dict()
        node = {}
        node['parent'] = None
        node['action'] = None
        node['state'] = state
        path.put(node)

        best_score = 0
        bfs_score = []

        while not path.empty():
            node = path.get()
            state = node['state']
            if explored.has_key(state):
                continue

            explored[state] = True
            if state.isWin():
                break

            for childState, action in successors:
                if not explored.has_key(childState):
                    if childState.isWin() or childState.isLose():
                        return action
                    sub_node = {}
                    sub_node['parent'] = node
                    sub_node['action'] = action
                    sub_node['state'] = childState
                    path.put(sub_node)

        while node['action'] != None:
            score = scoreEvaluation(node['state'])
            best_score = best_score + score
            node = node['parent']

        return best_score

class DFSAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write DFS Algorithm instead of returning Directions.STOP
        legal = state.getLegalPacmanActions()
        successors = [(state.generateSuccessor(0, action), action) for action in legal]

        bestScore = []
        for state, action in successors:
            if state.isWin() or state.isLose():
                return action
            bestScore.append((DFSAgent.dfs(self, state), action))

        dfs_best = max(bestScore)[0]
        dfs_action = [pair[1] for pair in bestScore if pair[0] == dfs_best]

        # if len(dfs_action) > 1:
        #     return random.choice(dfs_action)
        # else:
        #     return dfs_action[0]
        return dfs_action[0]

    # Perform dfs on each state and return best score
    def dfs(self, state):
        legal = state.getLegalPacmanActions()
        successors = [(state.generateSuccessor(0, action), action) for action in legal]

        path = Queue.LifoQueue()
        explored = dict()
        node = {}
        node['parent'] = None
        node['action'] = None
        node['state'] = state
        path.put(node)

        best_score = 0
        dfs_score = []

        while not path.empty():
            node = path.get()
            state = node['state']
            if explored.has_key(state):
                continue

            explored[state] = True
            if state.isWin():
                break

            for childState, action in successors:
                if not explored.has_key(childState):
                    if childState.isWin() or childState.isLose():
                        return action
                    sub_node = {}
                    sub_node['parent'] = node
                    sub_node['action'] = action
                    sub_node['state'] = childState
                    path.put(sub_node)

        while node['action'] != None:
            score = scoreEvaluation(node['state'])
            best_score = best_score + score
            node = node['parent']

        return best_score

class AStarAgent(Agent):
    # Initialization Function: Called one time when the game starts
    def registerInitialState(self, state):
        return;

    # GetAction Function: Called with every frame
    def getAction(self, state):
        # TODO: write A* Algorithm instead of returning Directions.STOP
        return Directions.STOP
