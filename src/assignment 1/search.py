# Netanel Bashan, 323056077, netanebashan12@gmail.com
# Elyasaf Dimant, 204006415, elyasafdi@gmail.com


#2.)        h1 hurisitcs results
#       omekMax3 == 230
#       average mispar bdikot 3 == 33.56
#
#       omekMax4 == 115,304
#       average mispar bdikot 4 == 10,148.25
#
#
#4.)        h2 hurisitcs results
#       omekMax3 == 76
#       average mispar bdikot 3 == 23.5
#
#       omekMax4 == 113,520
#       average mispar bdikot 4 == 4094.64
#
#          CONCLUSIONS:
#   A* using h2 manhaton is more optimal than using h1
#   WE CAN SEE IT BY THAT EVERY CATEGORY IN H2 IS SMALLER THAN H1


#search
import state
import frontier

def search(n,i):
    s=state.create(n)
    print(s)
    print(i)
    f = frontier.create(s)
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        if state.is_target(s):
            return [s, f[1], f[3]]
        ns=state.get_next(s)
        for i in ns:
            frontier.insert(f,i)
    return 0
# the maximum depth average for a 3 by 3 size board
omekMax3 = 0
# the maximum depth average for a 4 by 4 size board
omekMax4 = 0
# the average number of tests for a 3 by 3 size board
misBdik3 = 0
# the average number of tests for a 4 by 4 size board
misBdik4 = 0

# A loop that runs the algorithm 100 times<
# calculates the required averages.
# At the end of the program the averages are printed.
# Also for the convenience of the debugging operation we printed out the state itself each time
for i in range(100):
    _3 = search(3,i)
    _4 = search(4,i)
    misBdik3 += _3[1]
    misBdik4 += _4[1]
    if(_3[2]> omekMax3):
        omekMax3 = _3[2]
    if (_4[2] > omekMax4):
        omekMax4 = _4[2]

print("omekMax3:\n")
print(omekMax3)
print("omekMax4\n")
print(omekMax4)
print("averageMisBdik3\n")
print(misBdik3/100)
print("averageMisBdik4\n")
print(misBdik4/100)


