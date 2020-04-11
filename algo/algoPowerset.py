# powerset means every possible subset including empty set

def generatePowerSet(xs):
    result = [[]]
    for x in xs:
        newSubSet = [c + [x] for c in result]
        result.extend(newSubSet)
    return result


def generatePowerSet2(orig, newset):
    if orig == []:
        return [newset]
    else:
        res = []
        for s in generatePowerSet2(orig[1:], newset + [orig[0]]):
            res.append(s)
        for s in generatePowerSet2(orig[1:], newset):
            res.append(s)
        return res


def generatePowerSet3(orig, newset):
    if orig == []:
        yield newset
    else:
        for s in generatePowerSet2(orig[1:], newset + [orig[0]]):
            yield s
        for s in generatePowerSet2(orig[1:], newset):
            yield s


def generatePowerSet4(lst):
    if len(lst) <= 1:
        yield lst
        yield []
    else:
        for s in generatePowerSet4(lst[1:]):
            yield [lst[0]] + s
            yield s

# bitwise operators
def generatePowerSet5(lst):
    pairs=[(2**i,x) for i,x in enumerate(lst)]
    for i in range(2**len(pairs)):
        yield [x for (mask,x) in pairs if i & mask]

from math import log
def binaryRepresentation(num):
    for i in range(num):
        b=str(bin(i))[2:]
        # if num%2!=0:
        #     lnt=int(1.0+len(str(num)))
        # else:
        #     lnt=int(log(num,2))
        # b='0'*(lnt-len(b))+b
        print(b)

lst = [1, 2, 3]
print("generator powerset example")
print("method1", generatePowerSet(lst))
print("method2", generatePowerSet2(lst, []))
method3Res = [c for c in generatePowerSet3(lst, [])]
print("method3", method3Res)
print("method3", list(generatePowerSet3(lst, [])))
print("method4", list(generatePowerSet4(lst)))
print("method5", list(generatePowerSet5(lst)))

print("binary representation", binaryRepresentation(9))
