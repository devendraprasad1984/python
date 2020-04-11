# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

def testDivNum(num1,num2):
    arr=[]
    for i in range(num1,num2):
        if (i%7==0) and (i%5!=0):
            arr.append(str(i))
    return arr

arr=testDivNum(100,200)
print("divisble by 7 and not by 5",arr)
print("divisble by 7 and not by 5 separated by comma",(','.join(arr)))
