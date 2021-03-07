#search
import state
import frontier


#hello world yo yo yoyy
def search(n,i):
    s=state.create(n)
    print(s)
    print(i)
    f=frontier.create(s)
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        if state.is_target(s):
            return [s, f[1], f[3]]
        ns=state.get_next(s)
        for i in ns:
            frontier.insert(f,i)
    return 0




omekMax3 = 0
omekMax4 = 0
misBdik3 = 0
misBdik4 = 0

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