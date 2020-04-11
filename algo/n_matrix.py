"""
        if n=3 prepare matrix like
        3     3     3     3     3
        3     2     2     2     3
        3     2     1     2     3
        3     2     2     2     3
        3     3     3     3     3
"""

n=3
loop=n*2-1
num=n
square=[[n for i in range(loop)] for j in range(loop)]
# for i in range(loop):
#     for j in range(loop):
#         print(j,num,'\t',end=" ")
#     print("")

# print(square)
i=0
for row in square:
    j=0
    for col in row:
        if (j>0 and j<loop-1) and (i>0 and i<loop-1):
            print(col-1,end=" ")
        else:
            print(col,end=" ")
        j+=1
    i+=1
    print("")

