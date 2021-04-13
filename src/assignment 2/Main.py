# Netanel Bashan, 323056077, netanebashan12@gmail.com
# Elyasaf Dimant, 204006415, elyasafdi@gmail.com
import BritishMuseum
import ForwardChecking
import HeuristicRepair

BritishCounter_4 = 0
BritishCounter_6 = 0
ForwardCounter_maxN = 27
HeuristicAverage_27 = 0
BritishCounter_15 = 0
ForwardIterations_15 = 0
ForwardMoves_15 = 0
HeuristicAverage_15 = 0


for i in range(20):
    BritishCounter_4 += BritishMuseum.start(4)
    BritishCounter_6 += BritishMuseum.start(6)
    HeuristicAverage_27 += HeuristicRepair.start(ForwardCounter_maxN)
    BritishCounter_15 += BritishMuseum.start(15)
    ForwardIterations_15temp, ForwardMoves_15temp = ForwardChecking.start(15)
    ForwardIterations_15 += ForwardIterations_15temp
    ForwardMoves_15 += ForwardMoves_15temp
    HeuristicAverage_15 += HeuristicRepair.start(15)

ForwardIterator, ForwardMoves = ForwardChecking.start(ForwardCounter_maxN)

print("Question 2:")
print("BritishMuseum:")
print("Average iterations in British (4) = ", BritishCounter_4 / 20)
print("Average iterations in British (6) = ", BritishCounter_6 / 20)

print("Question 3:")
print("Forward Checking:")
print("As remember the counters of DFS were:")
print("# of iterations: 982")
print("# of queens placed + backtracks: 218")
print("How much did you save compared to the simple DFS algorithm ?")
print("Answer: None!")
print("         number_of_iterations: ", ForwardIterator)
print("         number_of_moves: ", ForwardMoves)
print("To what extent did you manage to get a solution ?")
print("Answer: n = ", ForwardCounter_maxN)

print("Question 4:")
print("Heuristic Repair:")
print("Were you able to improve the average performance of 20 runs across the algorithm with Forward Checking ?")
print("Answer: Yes!, now the average is: ", HeuristicAverage_27 / 20)

print("Question 5:")
print("What were the values of your masses for n = 15 on average?")
print("Answer:")
print("British: ", BritishCounter_15 / 20)
print("Forward: ", "number_iterations: ", ForwardIterations_15 / 20)
print("         number_moves: ", ForwardMoves_15 / 20)
print("Heuristic: ", HeuristicAverage_15 / 20)
