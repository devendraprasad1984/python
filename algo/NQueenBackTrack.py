"""
What is backtracking?
Backtracking is finding the solution of a problem whereby the solution depends on the previous steps taken.
For example, in a maze problem, the solution depends on all the steps you take one-by-one. If any of those steps is wrong, then it will not lead us to the solution. In a maze problem, we first choose a path and continue moving along it. But once we understand that the particular path is incorrect, then we just come back and change it. This is what backtracking basically is.
In general, this is accomplished by recursion
Thus, in backtracking, we first start with a partial sub-solution of the problem (which may or may not lead us to the solution) and then check if we can proceed further with this sub-solution or not. If not, then we just come back and change it.

One of the most common examples of the backtracking is to arrange N queens on an NxN chessboard such that no queen
can strike down any other queen. A queen can attack horizontally, vertically, or diagonally. The solution to this problem
is also attempted in a similar way. We first place the first queen anywhere arbitrarily and then place the next queen in
any of the safe places. We continue this process until the number of unplaced queens becomes zero (a solution is found)
or no safe place is left. If no safe place is left, then we change the position of the previously placed queen.

complexity: T(n) = n*T(n-1) + O(n^2) which translates to O(N!) time complexity in average.
And if you need all the possible solutions, the best, average and worst case complexity remains O(N!)
Now number of possible arrangements of N Queens on N x N chessboard is N!, given you are skipping row or column, already having a queen placed.
So average and worst case complexity of the solution is O(N!) (since, you are checking all
the possible solutions i.e. NNarrangements). The best case occurs if you find your solution
before exploiting all possible arrangements. This depends on your implementation.

"""


N=4
# board=[[0 for _ in range(N)] for _ in range(N)]
board=[[0]*N for _ in range(N)]

def isSafe(i,j):
    for x in range(0,N):
        #check row and columns for safety
        if board[i][x]==1 or board[x][j]==1:
            return False
        #check diagonal
        for x in range(0,N):
            for y in range(0,N):
                if x+y==i+j or x-y==i-j:
                    if board[x][y]==1:
                        return False
    return True

def placeQueen(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if isSafe(i,j) and board[i][j]!=1:
                board[i][j]=1
                if placeQueen(n-1):
                    return True
                board[i][j]=0
    return False

def printX(board):
    for i in board:
        print(i)

placeQueen(N)
printX(board)


