"""
Search in row wise, column wise sorted matrix
{10, 20, 30, 40}
{15, 25, 35, 45}
{27, 29, 37, 48}
{32, 33, 39, 50}
"""

arr=[
    [10, 20, 30, 40]
    ,[15, 25, 35, 45]
    ,[27, 29, 37, 48]
    ,[32, 33, 39, 50]
]

print(arr)

found=False
num=37
for r in arr:
    for c in r:
        if c==num:
            found=True
            print("found at ",num,"->",r)
            break

if found==False:
    print(num,"cannot be found")

