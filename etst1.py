a=list('12345678')
a[0]=a[6]=0
a[1]=a[-7]
a=int(''.join([str(i) for i in a]))
print(a)

a=[(j**2)*10**(2-i) for (i,j) in enumerate(range(1,4))]
print(sum(a))

foo=[2,18,9,22,17,24,8,12,27]
a=list(filter(lambda x:x%3==0,foo))
a=list(filter(lambda x:x%2==0,foo))
a=map(lambda x:x*2,a)
print(list(a))

def func(a):
    c=a
    c[0]+=51

b=[1000]
print(b[0])
func(b)
print(b[0])

print([1,2,2]*-2)
# print([1,2,3,4,5]-[1, 2, 3, 4, 5])
print('good'+'good'[::-1])

b='abcd'
for i in range(len(b)-2):
    b[i].upper()
print(b)


def func1(a,b):
    if b==0:
        return  a
    else:
        return func1(a^b,(a&b)<<1)

print(func1(5,6))



foo=[2]
foo+=[10]
print(min(foo))



def generatePowerSet(lst):
    pairs=[(2**i,x) for i,x in enumerate(lst)]
    for i in range(2**len(pairs)):
        newList=[x for (mask,x) in pairs if i & mask]
        if newList.__len__()==2:
            yield newList



print(list(generatePowerSet([1,2,3])))
