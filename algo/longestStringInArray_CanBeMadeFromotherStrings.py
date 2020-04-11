"""

"""

arr=["geeks","for","geeksgeeks","geeksfor","geeksforgeeks"]
maxStr=sorted(arr,key=lambda x:-len(x))[0]
print(arr,maxStr)
found=False
for x in arr:
    for y in arr:
        if maxStr!=x and maxStr!=y:
            # print(x+y)
            if x+y==maxStr:
                found=True
                print("max string",maxStr,"is possible to built from parts of arrays",x,y)
                break

if not found:
    print("max string",maxStr,"is not possible to built from parts of arrays")