"""
7
UK
China
USA
France
New Zealand
UK
France
Sample Output
5
Explanation: UK and France repeat twice. Hence, the total number of distinct country stamps is  (five).
"""

stamps=set()
n=int(input())
for x in range(n):
    sx=input()
    stamps.add(sx)
print(len(stamps))
