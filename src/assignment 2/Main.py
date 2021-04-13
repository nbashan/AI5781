# Netanel Bashan, 323056077, netanebashan12@gmail.com
# Elyasaf Dimant, 204006415, elyasafdi@gmail.com
import BritishMuseum
import ForwardChecking
import HeuristicRepair

BritishCounter_4 = 0
BritishCounter_6 = 0
ForwardCounter_maxN = 27
HeuristicAverage_27 = 0
# BritishCounter_15 = 0
ForwardIterations_15 = 0
ForwardMoves_15 = 0
HeuristicAverage_15 = 0


for i in range(20):
    BritishCounter_4 += BritishMuseum.start(4)
    BritishCounter_6 += BritishMuseum.start(6)
    HeuristicAverage_27 += HeuristicRepair.start(ForwardCounter_maxN)
    # BritishCounter_15 += BritishMuseum.start(15)
    ForwardIterations_15temp, ForwardMoves_15temp = ForwardChecking.start(15)
    ForwardIterations_15 += ForwardIterations_15temp
    ForwardMoves_15 += ForwardMoves_15temp
    HeuristicAverage_15 += HeuristicRepair.start(15)

ForwardIterator, ForwardMoves = ForwardChecking.start(ForwardCounter_maxN)
ForwardIterator_8, ForwardMoves_8 = ForwardChecking.start(8)

print()
print("Question 2:")
print("British Museum:")
print("Average iterations in British (4) = ", BritishCounter_4 / 20)
print("Average iterations in British (6) = ", BritishCounter_6 / 20)

print()
print("Question 3:")
print("Forward Checking:")
print("As remember the counters of DFS were:")
print("# of iterations: 982")
print("# of queens placed + backtracks: 218")
print("Q: How much did you save compared to the simple DFS algorithm ?")
print("A: None!")
print("         # of iterations: ", ForwardIterator_8)
print("         # of queens placed + backtracks: ", ForwardMoves_8)
print("Q: To what extent did you manage to get a solution ?")
print("A: n = ", ForwardCounter_maxN)

print()
print("Question 4:")
print("Heuristic Repair:")
print("Q: Were you able to improve the average performance of 20 runs across the algorithm with Forward Checking ?")
print("A: Yes!, # of iterations using Forward Checking was: ", ForwardIterator, " (when size = 27)")
print("now, using the heuristic, the average is: ", HeuristicAverage_27 / 20)

print()
print("Question 5:")
print("Q: What were the values of your counters for n = 15 on average?")
print("A:")
# print("British: ", BritishCounter_15 / 20)
print("Forward: ", "# of iterations: ", ForwardIterations_15 / 20)
print("          # of moves: ", ForwardMoves_15 / 20)
print("Heuristic: # of iterations: ", HeuristicAverage_15 / 20)

# Question 2:
# British Museum:
# Average iterations in British (4) =  155.75
# Average iterations in British (6) =  10725.05
#
# Question 3:
# Forward Checking:
# As remember the counters of DFS were:
# # of iterations: 982
# # of queens placed + backtracks: 218
# Q: How much did you save compared to the simple DFS algorithm ?
# A: None!
#          # of iterations:  982
#          # of queens placed + backtracks:  218
# Q: To what extent did you manage to get a solution ?
# A: n =  27
#
# Question 4:
# Heuristic Repair:
# Q: Were you able to improve the average performance of 20 runs across the algorithm with Forward Checking ?
# A: Yes!, # of iterations using Forward Checking was:  4796458  (when size = 27)
# now, using the heuristic, the average is:  3302.5
#
# Question 5:
# Q: What were the values of your counters for n = 15 on average?
# A:
# Forward:  # of iterations:  19329.8
#           # of moves:  2416.1
# Heuristic: # of iterations:  3420.95
