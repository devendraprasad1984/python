from itertools import permutations, combinations, combinations_with_replacement
print("permutations")
ix="HACK 2".split()
s=ix[0]
n=int(ix[1])
p=list(permutations(s,n))
ls=[''.join(x) for x in p]
ls.sort(key=lambda x:x)
for x in ls:
    print(x)

s="ABCD"
n=3
print("combinatons")
for i in range(1,n+1):
    c=list(combinations(sorted(s),i))
    c1=[''.join(x) for x in c]
    ls=[]
    for x in c1:
        ls.append(x)
    ls.sort(key=lambda x:x)
    print("\n".join(ls))




print("combination with replacements")
ix="HACK 2".split()
s=ix[0]
n=int(ix[1])
p=list(combinations_with_replacement(sorted(s),n))
ls=[''.join(x) for x in p]
ls.sort(key=lambda x:x)
for x in ls:
    print(x)

s, k = "HACK 2".split()
for c in combinations_with_replacement(sorted(s), int(k)):
    print("".join(c))