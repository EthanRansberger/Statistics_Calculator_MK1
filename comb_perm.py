def combinations(n,r):
    c = math.factorial(n)/(math.factorial(r)*math.factorial(n-r))
    print(c)
    return c
def permutations(n,r):
    perm=math.factorial(n)/math.factorial(n-1)
    print(perm)
    return perm
t=input("p or c?")
n=input("n objects?")
r=input("choosing objects?")
if t='p':
    permutations(n,r)
else:
    combinations(n,r)