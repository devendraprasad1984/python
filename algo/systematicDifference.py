"""
Task
Given  sets of integers,  and , print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

Input Format

The first line of input contains an integer, .
The second line contains  space-separated integers.
The third line contains an integer, .
The fourth line contains  space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

4
2 4 5 9
4
2 4 11 12
Sample Output

5
9
11
12
"""
# n1,s1=int(input()), list(map(int,input().split()))
# n2,s2=int(input()), list(map(int,input().split()))
n1,xs1=int("4"), set(list("2 4 5 9".split()))
n2,xs2=int("4"), set(list("2 4 11 12".split()))
# print(s1,s2,s1.intersection(s2),s1.union(s2),s1.difference(s2),s2.difference(s1))
sdiff=[]
sdiff.append([int(x) for x in xs1.difference(xs2)])
sdiff.append([int(x) for x in xs2.difference(xs1)])
print(sdiff)
arr=[]
for x in sdiff:
    for y in x:
        arr.append(y)
# arr.sort(lambda x:x)
# print('\n'.join(sorted(arr,lambda x:x)))
print('\n'.join([str(x) for x in sorted(arr,key=lambda x:x)]))
# print("diffs",xs1^xs2,'\n'.join(xs1^xs2),sdiff)
# xx=[[y for y in x] for x in sdiff]
# print(xx)
# print("\n".join([x for x in sdiff]))
# print(sdiff)
# xr=[]
# for x in sdiff:
#     for y in x:
#         xr.append(y)
# xr.sort(key=lambda x:x)
# print(xr,'\n'.join(xr))
# print("\n".join(xr))
# for x in xr:
#     print(x)


# a,b = [set(raw_input().split()) for _ in range(4)][1::2]
# print '\n'.join(sorted(a^b, key=int))
