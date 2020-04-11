"""
Given 3 points in below triangle, find wheather these 3 points are forming equalaterial triangle?
                (5,12,14) = true
                (6,18,22) = true
                (2,11,15) = false
"""
from math import *

arr=[[5,12,14],[6,18,22],[2,11,15]]
for i in arr:
    A,B,C=i[0],i[1],i[2]
    print(A,B,C,"triangle" if (A+B>=C and B+C>=A and A+C>=B) else "not Triangle")
    A1 = degrees(acos((B**2 + C**2 - A**2)/(2*B*C)))
    B1 = degrees(acos((C**2 + A**2 - B**2)/(2*C*A)))
    C1 = degrees(acos((A**2 + B**2 - C**2)/(2*A*B)))
    print(A1,B1,C1)