
def perm1(lst):
    if len(lst)==0:
        return []
    elif len(lst)==1:
        return lst
    else:
        l=[]
        for i in range(len(lst)):
            x=lst[i]
            xs=lst[:i]+lst[i+1:]
            for p in perm1(xs):
                l.append([x]+list(p))
        return l

# this is most efficient as yield is used, almost no memory is used to store the resultset
def perm2(lst):
    if len(lst)==0:
        yield []
    elif len(lst)==1:
        yield lst
    else:
        for i in range(len(lst)):
            x=lst[i]
            xs=lst[:i]+lst[i+1:]
            for p in perm2(xs):
                yield [x]+p

data=list('abcde')
print("permutation logic 1")
for p in perm1(data):
    print(p)

# relatively faster than logic 1 with large strings to permutate on
print("permutation logic 2")
for p in perm2(data):
    print(p)

