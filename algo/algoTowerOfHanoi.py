# tower of hanoi
# move n pieces from source to destination using a temporary location

def hanoi(n, src, dest, tmp):
    if n==0:
        pass
    else:
        for h in hanoi(n-1,src,tmp,dest):
            yield h
        yield src, dest
        for h in hanoi(n-1,tmp,dest,src):
            yield h

res_of_hanoi=hanoi(3,1,3,2)
print([c for c in res_of_hanoi])

res_of_hanoi=hanoi(3,1,3,2)
for c in res_of_hanoi:
    print(c)