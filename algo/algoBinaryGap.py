"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.
For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.
Write a function:
def solution(N)
that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.
For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
Write an efficient algorithm for the following assumptions:
N is an integer within the range [1..2,147,483,647].
"""


def binaryRepresentationInRange(num):
    for i in range(num):
        b = str(bin(i))[2:]
        print(b)

def getBinaryNum(num):
    zeroCount=oneCount=0
    binaryNum = str(bin(num))[2:]
    for i in range(0,len(binaryNum)):
        # print(binaryNum[i])
        if(int(binaryNum[i])==0): zeroCount+=1
        if(int(binaryNum[i])==1): oneCount+=1
    return "number: "+str(num),binaryNum,zeroCount,oneCount

def getLongestBinaryGapNum(binNum):
    longestGapNum=0
    iVal=0
    gotOneAgainInLoop=False
    boolObj={0:0,1:0}
    # print(boolObj.get(0),boolObj.get(1))
    zeroCount=oneCount=0
    for i in range(0,len(binNum)):
        iVal=int(binNum[i])
        if(iVal==1 and gotOneAgainInLoop==True):
            boolObj[0]=max(zeroCount,boolObj.get(0))
            gotOneAgainInLoop=False
            zeroCount=oneCount=0

        if(iVal==0): zeroCount+=1
        if(iVal==1):
            oneCount+=1
            gotOneAgainInLoop=True
    longestGapNum=boolObj[0]
    boolObj[1]=boolObj.get(1)
    return longestGapNum,boolObj[1]



# binaryRepresentationInRange(9)
# binaryRepresentationInRange(543)
print(getBinaryNum(9),getBinaryNum(529),getBinaryNum(20),getBinaryNum(15),getBinaryNum(32),getBinaryNum(1041),getBinaryNum(1),getBinaryNum(2147483647))
num2checkBinaryGapIn=32
binaryNumber=getBinaryNum(num2checkBinaryGapIn)[1]
# print(binaryNumber)
resOfLongestBinaryGap=getLongestBinaryGapNum(binNum=binaryNumber)
print("result of longest binaryGap in",binaryNumber,"is",resOfLongestBinaryGap)
