"""
you have m*n matrix like situation
you have to start at 0 every time and find out all possible routes from 0 to end
The problem is to print all the possible paths from top left to bottom right of a mXn matrix with the constraints that from each cell you can either move only to right or down.
Examples :

Input : 1 2 3
        4 5 6
Output : 1 4 5 6
         1 2 5 6
         1 2 3 6

Input : 1 2
        3 4
Output : 1 2 4
         1 3 4
The algorithm is a simple recursive algorithm, from each cell first print all paths by going down and then print all paths by going right. Do this recursively for each cell encountered.
"""
counter=0
def initBoard():
    board=[[0]*n for _ in range(m)]
    return board

def findPathRecurse(board,r,c,path, curIndex):
    global counter
    counter+=1
    #reaching at bottom loop in all columns ie move right
    if r==m-1:
        for k in range(c,n):
            path[curIndex+k-c]=str(r)+","+str(k)
        print("counter: ",counter,path)
        return
    # reaching right move in bottom
    if c==n-1:
        for k in range(r,m):
            path[curIndex+k-r]=str(k)+","+str(c)
        print("counter: ",counter,path)
        return
    path[curIndex]=str(r)+","+str(c)
    #move down recursively
    findPathRecurse(board,r+1,c,path,curIndex+1)
    #move down recursively
    findPathRecurse(board,r,c+1,path,curIndex+1)

m,n=3,4
board=initBoard()
path=[0 for d in range(m+n-1)] #total possible paths in mxn matrix
findPathRecurse(board,0,0,path,0)



