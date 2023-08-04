import math
def combinations(n,r):
    c = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
    print(c)
    return c
def permutations(n,r):
    perm=math.factorial(n)/math.factorial(n-1)
    print(perm)
    return perm
t=input("p or c?: ")
n=int(input("n objects?: "))
r=int(input("r choosing objects?: "))
if t=='p':
    permutations(n,r)
else:
    combinations(n,r)
