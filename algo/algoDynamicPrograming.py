# Q. How would you, in general terms, describe dynamic programming? As an example, how would you find the length of the longest common subsequence of elements in two arrays by using this method?
# A. Dynamic programming is a paradigm for solving optimization problems. It consists of finding solutions for intermediate subproblems, which can be stored and reused for solving the actual problem. Dynamic programming is the best approach for difficult problems that always become trivial once we know the solution for a slightly easier instance of that problem - the intermediate subproblem. Dynamic programming solutions are best represented by a recursive relation, and easily implemented.
# If the intermediate subproblems are not overlapping, then we have just a case of Divide and Conquer.
# Finding the longest common subsequence (LCS) between two arrays is a classical example of using dynamic programming. Let the arrays have lengths M and N, and stored as variables a[0:M] and b[0:N]. Let’s use L[p, q] to mark the length of the LCS for subarrays a[0:p] and b[0:q]; that is, L[p, q] == LCS(a[0:p], b[0:q]). Let’s also visualize what a matrix L[p, q] would look like for an example pair of “bananas” and “sandal”.

# p/q	0	1 B	2 A	3 N	4 A	5 N	6 A	7 S
# 0	0	0	0	0	0	0	0	0
# 1 S	0	0	0	0	0	0	0	1
# 2 A	0	0	1	1	1	1	1	1
# 3 N	0	0	1	2	2	2	2	2
# 4 D	0	0	1	2	2	2	2	2
# 5 A	0	0	1	2	3	3	3	3
# 6 L	0	0	1	2	3	3	3	3
# If p or q is zero, then L[p, q] = 0 since we have one empty subarray. All other fields have a simple rule connecting them - L[p, q] equals to the maximum value of the following options:
#
# L[p - 1, q] - the LCS didn’t change, we just added one letter to array a to achieve L[p, q]
# L[p, q - 1] - analogous for array b
#     L[p - 1, q - 1]+1 - adding the same letter to both a and b, which of course can’t happen for every field
#     If you look at the table again, you can see that numbers are always equal to the maximum of their upper or left neighbor, unless the values in that field are equal, in which case they increment that maximum by 1. So a solution to the problem is given with the following algorithm.
#
# FUNCTION lcs(a, b)
# M = a.length()
# N = b.length()
# L = Matrix[M + 1, N + 1]
# FOR i IN [0..M]
# L[i, 0] = 0
# END FOR
# FOR i IN [0..N]
# L[0, i] = 0
# END FOR
# FOR i IN [1..M]
# FOR j IN [1..N]
# L[i, j] = max(L[i-1, j], L[i, j-1])
# IF a[i-1] == b[j-1]
# L[i, j] = max(L[i, j], L[i-1, j-1] + 1)
# END IF
# END FOR
# END FOR
# RETURN L[M, N]
# The time complexity of this solution is O(MxN)

# dynamic programming greedy/bottom up/knapsack algo - get min coins possible for exchange
def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed,change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

def method3OfCoinsProble(changeAmount, coinsList, coins_so_far):
    if coinsList==[]:
        pass
    elif(sum(coins_so_far))==changeAmount:
        yield coins_so_far
    elif sum(coins_so_far) > changeAmount:
        pass
    else:
        for c in method3OfCoinsProble(changeAmount, coinsList[:], coins_so_far + [coinsList[0]]):
            yield c
        for c in method3OfCoinsProble(changeAmount, coinsList[1:], coins_so_far):
            yield c

def method4RecursiveChange(to_return,validCoinsList):
    flag=None
    for c in validCoinsList:
        if c==to_return: return c
        elif c<to_return: flag=c
    remainingBalance=to_return-flag
    return [flag]+[method4RecursiveChange(remainingBalance,validCoinsList)]

def flatten(listOfNestedArray):
    for item in listOfNestedArray:
        try:
            yield from flatten(item)
        except Exception:
            yield item



def minCoinsMainMethod():
    coin2Extract = 170
    listOfValidCoins=[1, 5, 10,20, 25,50]
    # method 2 solution
    coinsUsed = [0] * (coin2Extract + 1)
    coinCount = [0] * (coin2Extract + 1)
    result = dpMakeChange(listOfValidCoins,coin2Extract,coinCount,coinsUsed)
    print("max optimal METHOD2: total min num of coins to get", coin2Extract, "is: ", result)
    # print("coins used array",coinsUsed)
    printCoins(coinsUsed,coin2Extract)

    # # method 3 solution
    # solution=[s for s in method3OfCoinsProble(coin2Extract,listOfValidCoins,[])]
    # # for s in solution:
    # #     print("possible combinations",s)
    # minCoinsArray=min(solution,key=len)
    # print("less optimal METHOD3: min coins to be used to extract",coin2Extract,minCoinsArray,"having total",minCoinsArray.__len__(),"coins")

    # method4 to return the in min best possible way
    # greedy Algo
    result=method4RecursiveChange(coin2Extract,listOfValidCoins)
    list_result=list(flatten(result))
    print("max optimal METHOD4: min coins to be used to extract",coin2Extract,list_result,"having total",list_result.__len__(),"coins")


def lcsUsingRecursion(xlist, ylist):
    # longest common subsequence, this is worst performing, hence using dynamic programming will be best for optimal solutions
    if not xlist or not ylist:
        return []
    x,xs, y, ys=xlist[0],xlist[1:],ylist[0],ylist[1:]
    if x==y:
        return [x] + lcsUsingRecursion(xs, ys)
    else:
        return max(lcsUsingRecursion(xlist, ys), lcsUsingRecursion(ylist, xs), key=len)

def lcsUsingDynamicProgramming(xlist,ylist):
    # make row column matrix from 2 strings
    matrix=[[0 for j in range(len(ylist)+1)] for i in range(len(xlist)+1)]
    for i,x in enumerate(xlist):
        for j,y in enumerate(ylist):
            if x==y:
                matrix[i+1][j+1]=matrix[i][j]+1
            else:
                matrix[i+1][j+1]=max(matrix[i+1][j],matrix[i][j+1])
    #capturing result
    result=[]
    x,y=xlist.__len__(),ylist.__len__()
    while x>0 and y>0:
        if matrix[x][y]==matrix[x-1][y]:
            x-=1
        elif matrix[x][y]==matrix[x][y-1]:
            y-=1
        else:
            result=[xlist[x-1]]+result
            x-=1
            y-=1
    return result, matrix


import string,random
import numpy as np
def generateRandomSequenceOfString(numberOfChars, strChars=string.ascii_uppercase):
    for i in range(numberOfChars):
        yield random.choice(strChars)

if __name__ == '__main__':
    print("we are working on min coins program")
    minCoinsMainMethod()

    print("we are working on lcs-longest common subsequence")
    s1=[c for c in generateRandomSequenceOfString(10,'ADAD')]
    s2=[c for c in generateRandomSequenceOfString(10,'ADAD')]
    print("string 1 = ",s1)
    print("string 2 = ",s2)
    # resOfLCS=lcsUsingRecursion(s1, s2)
    # print("lcs result is", resOfLCS,"having length of",resOfLCS.__len__(),"chars")
    resOfLCS,matrixOfStrings=lcsUsingDynamicProgramming(s1, s2)
    print("results of lcs are",resOfLCS,"of length",resOfLCS.__len__(),"chars")
    print("matrix of lcs are\n",np.array(matrixOfStrings))
    # print("lcs result is", resOfLCS,"having length of",resOfLCS.__len__(),"chars")

