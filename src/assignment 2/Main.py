# Netanel Bashan, 323056077, netanebashan12@gmail.com
# Elyasaf Dimant, 204006415, elyasafdi@gmail.com
import BritishMuseum
import ForwardChecking
import HeuristicRepair
import DfsBackTracking

# Main program that centralized the runs of all the algorithms,
# according to the requirements in the exercise file

# For running the British-Museum algorithm with size =  4,
# for calculates the average number of iterations
BritishCounter_4 = 0

# For running the British-Museum algorithm with size =  6,
# for calculates the average number of iterations
BritishCounter_6 = 0

# For running the Forward-Checking algorithm with max size we have achieved =  27
ForwardCounter_maxN = 27

# For running the Forward-Checking algorithm with max size we have achieved,
# For calculates the average number of iterations
HeuristicAverage_27 = 0

# For running the British-Museum algorithm with size = 15
# For calculates the average number of iterations
# (The British algorithm (15) took way too long so we did not run it because it stuck the run!)
# BritishCounter_15 = 0

# For running the Forward-Checking algorithm with size = 15
# For calculates the average number of iterations & number of moves
ForwardIterations_15 = 0
ForwardMoves_15 = 0

# For running the Heuristic-Repair algorithm with size = 15
# For calculates the average number of iterations
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

# For calculates the average number of iterations & number of moves with size = 27,
# and compare it to the Heuristic algorithm
ForwardIterator, ForwardMoves = ForwardChecking.start(ForwardCounter_maxN)

# For calculates the average number of iterations & number of moves with size = 8 in Forward-Checking algorithm
# and compare it to the DFS algorithm
ForwardIterator_8, ForwardMoves_8 = ForwardChecking.start(8)

# For calculates the number of iterations & number of moves with size = 4 in Dfs-BackTracking algorithm,
DFSIterator_4, DFSMoves_4 = DfsBackTracking.start(4)

# For calculates the number of iterations & number of moves with size = 8 in Dfs-BackTracking algorithm,
# and compare it to the Forward-Checking algorithm
DFSIterator_8, DFSMoves_8 = DfsBackTracking.start(8)

print()
print("Question 1:")
print("Dfs-BackTracking:")
print("     size = 4:")
print("         # of iterations: ", DFSIterator_4)
print("         # of queens placed + backtracks: ", DFSMoves_4)
print("     size = 8:")
print("         # of iterations: ", DFSIterator_8)
print("         # of queens placed + backtracks: ", DFSMoves_8)

print()
print("Question 2:")
print("British Museum:")
print("     Average iterations in British (4) = ", BritishCounter_4 / 20)
print("     Average iterations in British (6) = ", BritishCounter_6 / 20)

print()
print("Question 3:")
print("Forward Checking:")
print("     As remember the counters of DFS were:")
print("         # of iterations: ", DFSIterator_8)
print("         # of queens placed + backtracks: ", DFSMoves_8)
print("     Q: How much did you save compared to the simple DFS algorithm ?")
print("     A: None!")
print("         # of iterations: ", ForwardIterator_8)
print("         # of queens placed + backtracks: ", ForwardMoves_8)
print("     Q: To what extent did you manage to get a solution ?")
print("     A: n = ", ForwardCounter_maxN)

print()
print("Question 4:")
print("Heuristic Repair:")
print("    Q: Were you able to improve the average performance of 20 runs across the algorithm with Forward Checking ?")
print("    A: Yes!, # of iterations using Forward Checking was: ", ForwardIterator, " (when size = 27)")
print("    now, using the heuristic, the average is: ", HeuristicAverage_27 / 20)

print()
print("Question 5:")
print("     Q: What were the values of your counters for n = 15 on average?")
print("     A:")
# print("     British: ", "# of iterations: ", BritishCounter_15 / 20)
print("     Forward: ", "# of iterations: ", ForwardIterations_15 / 20)
print("               # of moves: ", ForwardMoves_15 / 20)
print("     Heuristic: # of iterations: ", HeuristicAverage_15 / 20)
print("     (The British algorithm (15) took way too long so we did not run it because it stuck the run)")


# ##################################################---OUR RESULTS:---##################################################

# Question 1:
# Dfs-BackTracking:
#      size = 4:
#          # of iterations:  31
#          # of queens placed + backtracks:  12
#      size = 8:
#          # of iterations:  982
#          # of queens placed + backtracks:  218
#
# Question 2:
# British Museum:
#      Average iterations in British (4) =  151.9
#      Average iterations in British (6) =  12490.9
#
# Question 3:
# Forward Checking:
#      As remember the counters of DFS were:
#          # of iterations:  982
#          # of queens placed + backtracks:  218
#      Q: How much did you save compared to the simple DFS algorithm ?
#      A: None!
#          # of iterations:  982
#          # of queens placed + backtracks:  218
#      Q: To what extent did you manage to get a solution ?
#      A: n =  27
#
# Question 4:
# Heuristic Repair:
#     Q: Were you able to improve the average performance of 20 runs across the algorithm with Forward Checking ?
#     A: Yes!, # of iterations using Forward Checking was:  4796458  (when size = 27)
#     now, using the heuristic, the average is:  1687.45
#
# Question 5:
#      Q: What were the values of your counters for n = 15 on average?
#      A:
#      Forward:  # of iterations:  19329.8
#                # of moves:  2416.1
#      Heuristic: # of iterations:  1754.4
#      (The British algorithm (15) took way too long so we did not run it because it stuck the run)
