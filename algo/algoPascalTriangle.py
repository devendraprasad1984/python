# import numpy as np
#
# x=[0]*10
# y=[0]*5
# matrix=[[0 for c in x] for j in y]
# print(np.array(matrix))

def nck_multiplicative(n, k):
    result = 1
    for i in range(1, k + 1):
        result = int(result * (n - (k - i)) / i)
    return result

def simpleTriangle(n):
    for i in range(1, n + 1):
        stars=""
        spaces=""
        for j in range(int(n-i/2)):
            spaces=spaces+" "
        for j in range(i):
            stars=stars+"*"
        print(spaces+stars,)

simpleTriangle(10)

def print_center(sValues):
    maxLen = len(max(sValues, key=len))
    for i, s in enumerate(sValues):
        diff = maxLen - len(s)
        pad = ' ' * int(diff / 2)
        yield str(i) + '->' + pad + s

def pascal_triangle_main(num):
    allList = []
    for i in range(num):
        nList = []
        for j in range(i + 1):
            nList.append(nck_multiplicative(i, j))
        nList = ' '.join(map(str, nList))
        allList.append(nList)
    # print("pascal triangle in one line", allList)
    print("pascal triangle in list matrix form")
    for p in allList:
        print(p)
    print("pascal triangle in triangle form")
    for p in print_center(allList):
        print(p)

if __name__ == '__main__':
    pascal_triangle_main(5)