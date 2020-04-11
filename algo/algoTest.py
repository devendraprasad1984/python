def selectionSortTest(arr,breakAt):
    print("original array is",arr)
    for i in range(0,len(arr)-1):
        for j in range(i+1, len(arr)-1):
            if(arr[i]>arr[j]):
                print("swapping",arr[i],"with",arr[j])
                #swap the elements
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
        if(i==breakAt and breakAt!=-1):
            break
    print("array after",(breakAt+1),"iteration",arr)
    print("conclusion:smallest in array comes at its correct position after 1st run i.e start")

def bubbleSortTest(arr,breakAt):
    print("original array is",arr)
    for i in range(0,len(arr)-1):
        for j in range(1, len(arr)-1):
            if(arr[j]>arr[j+1]):
                print("swapping",arr[j],"with",arr[j+1])
                #swap the elements
                temp=arr[j+1]
                arr[j+1]=arr[j]
                arr[j]=temp
        if(i==breakAt and breakAt!=-1):
            break
    print("array after",(breakAt+1),"iteration",arr)
    print("conclusion:largest in array comes at its correct position after 1st run i.e. last")

def mergeSortTest(arr,breakAt):
    # this is divide and conquer algo
    print("splitting",arr)
    if(len(arr)>1):
        mid=len(arr)/2
        leftHalf=arr[0:int(mid)]
        rightHalf=arr[int(mid):len(arr)]
        print("left part:",leftHalf,"right part:",rightHalf)
        mergeSortTest(leftHalf,-1)
        mergeSortTest(rightHalf,-1)
        i = 0
        j = 0
        k = 0
        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]
                i = i + 1
            else:
                arr[k] = rightHalf[j]
                j = j + 1
            k = k + 1

        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i = i + 1
            k = k + 1

        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j = j + 1
            k = k + 1
    print("Merging ", arr)

# ----------------------------------

arr=[5,3,8,9,1,7,0,2,6,4]
print("------------------------")
print("selection sort")
selectionSortTest(arr,0)

arr=[5,3,8,9,1,7,0,2,6,4]
print("------------------------")
print("buble sort")
bubbleSortTest(arr,0)

arr=[5,3,8,9,1,7,0,2,6,4]
print("------------------------")
print("merge sort")
mergeSortTest(arr,0)




