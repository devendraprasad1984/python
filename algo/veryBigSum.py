"""
input
5
1000000001 1000000002 1000000003 1000000004 1000000005
Output: 5000000015
"""
import decimal

def aVeryBigSum(ar):
    # cnt=ar[0].__str__().__len__()
    # sumStr=[0 for i in range(cnt)]
    # print(sumStr)
    # for x in ar:
    #     for i in range(len(x.__str__())):
    #         sumStr[i]=int(sumStr[i])+int(x.__str__()[i])
    #     print("".join([str(x) for x in sumStr]))
    # retRes="".join([str(x) for x in sumStr])
    # # print(sumStr,retRes)
    # return retRes.strip("")
    sumStr=0
    for x in ar:
        sumStr+= decimal.Decimal(x)
    return sumStr

n=5
arrString="1000000001 1000000002 1000000003 1000000004 1000000005"
arrVals=arrString.split(" ")
result = aVeryBigSum(arrVals)
print(result)