"""
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

For example, given the array  there are  elements, two positive, two negative and one zero. Their ratios would be ,  and . It should be printed as

0.400000
0.400000
0.200000
Function Description

Complete the plusMinus function in the editor below. It should print out the ratio of positive, negative and zero items in the array, each on a separate line rounded to six decimals.

plusMinus has the following parameter(s):

arr: an array of integers
Input Format

The first line contains an integer, , denoting the size of the array.
The second line contains  space-separated integers describing an array of numbers .

Constraints



Output Format

You must print the following  lines:

A decimal representing of the fraction of positive numbers in the array compared to its size.
A decimal representing of the fraction of negative numbers in the array compared to its size.
A decimal representing of the fraction of zeros in the array compared to its size.
Sample Input

6
-4 3 -9 0 4 1
Sample Output

0.500000
0.333333
0.166667
Explanation

There are  positive numbers,  negative numbers, and  zero in the array.
The proportions of occurrence are positive: , negative:  and zeros: .
"""

# Complete the plusMinus function below.
import decimal
import math

def plusMinus(arr):
    zero,plus,minus=0,0,0
    cnt=arr.__len__()
    for x in arr:
        if x>0:
            plus+=1
        elif x<0:
            minus+=1
        else:
            zero+=1
    print(round(decimal.Decimal(plus/cnt),6))
    print(round(decimal.Decimal(minus/cnt),6))
    print(round(decimal.Decimal(zero/cnt),6))

if __name__ == '__main__':
    # n = int(input())
    # arr = list(map(int, input().rstrip().split()))
    plusMinus([1,1,0,-1,-1])



