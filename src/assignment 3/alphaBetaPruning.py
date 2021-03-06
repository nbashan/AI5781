# Netanel Bashan, 323056077, netanebashan12@gmail.com
# Elyasaf Dimant, 204006415, elyasafdi@gmail.com
import game

# depth if search in the tree
DEPTH = 2


# In this function we make a move of the smart agent by recursively calling the functions,
# to find the minimum and maximum according to the heuristic values we have set
def go(gm):
    # print("In go of game ", gm.board)
    # if its human 'turn' so we want to find the state with the min heuristic value
    if game.isHumTurn(gm):
        # print("Turn of human")
        # find the state with the min heuristic value
        obj = abmin(gm, DEPTH, game.LOSS - 1, game.VICTORY + 1)[1]
        # return
        return obj
    else:
        # print("Turn of agent")
        # if its out 'turn' so we want to find the state with the high heuristic value
        obj = abmax(gm, DEPTH, game.LOSS - 1, game.VICTORY + 1)[1]
        # return
        return obj


# s = the state (max's turn)
# d = max. depth of search
# alpha = 10**20 - 1 (generally uses to find the min)
# beta =  10**20 + 1 (generally uses to find the max)
# returns [v, ns]: v = state s's value. ns = the state after recommended move.
#        if s is a terminal state ns=0.


# In this function we look for the situation with the highest heuristic value from the next steps
def abmax(gm, d, a, b):
    # print("now calculate abmax")
    # d = depth of search at this call
    # alpha = 10**20 - 1
    # beta =  10**20 + 1

    # stop conditions: DEPTH = 0 (no more searches) or game-over
    if d == 0 or game.isFinished(gm):
        # print("returns ", [game.value(gm), gm])
        # return the heuristic value which determines if its loss, victory, tie or neither
        return [game.value(gm), gm]
    v = float("-inf")
    ns = game.getNext(gm)
    # print("next moves:", len(ns), " possible moves ")
    # loop over all states and found the state with the lowest heuristic value
    bestMove = 0
    for st in ns:
        # call to the next depth of search, there we want the lowest heuristic value
        tmp = abmin(st, d - 1, a, b)
        # we want to find the highest state's value(, so at start we init v with value of -infinity)
        # tmp[0] is the value of v we get from abmin
        if tmp[0] > v:
            v = tmp[0]
            bestMove = st
        # in this case we can make pruning because surely it the highest state's value in this branch
        if v >= b:
            return [v, st]
        # the wonted state's value is high then loss so we can do update
        # if v > a:
        #    a = v
    return [v, bestMove]


# s = the state (min's turn)
# d = max. depth of search
# alpha = 10**20 - 1 (generally uses to find the min)
# beta =  10**20 + 1 (generally uses to find the max)
# returns [v, ns]: v = state s's value. ns = the state after recommended move.
#        if s is a terminal state ns=0.

# In this function we look for the situation with the lowest heuristic value from the next steps
def abmin(gm, d, a, b):
    # print("now calculate abmin")
    # d = depth of search at this call
    # alpha = 10**20 - 1
    # beta =  10**20 + 1

    # stop conditions: DEPTH = 0 (no more searches) or game-over
    if d == 0 or game.isFinished(gm):
        # return the heuristic value which determines if its loss, victory, tie or neither
        return [game.value(gm), 0]
    v = float("inf")

    # list of next states
    ns = game.getNext(gm)
    # print("next moves:", len(ns), " possible moves ")
    # loop over all states and found the state with the lowest heuristic value
    bestMove = 0
    for st in ns:
        # call to the next depth of search, there we want the highest heuristic value
        tmp = abmax(st, d - 1, a, b)
        # we want to find the lowest state's value (, so at start we init v with value of +infinity)
        # tmp[0] is the value of v we get from abmax
        if tmp[0] < v:
            v = tmp[0]
            bestMove = st
        # in this case we can make pruning because surely it the lowest state's value in this branch
        if v <= a:
            return [v, st]
        # the wonted state's value is less then victory+1 so we can do update
        # if v < b:
        #    b = v
    return [v, bestMove]
