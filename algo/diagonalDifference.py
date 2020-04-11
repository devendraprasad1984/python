"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix  is shown below:

1 2 3
4 5 6
9 8 9
The left-to-right diagonal = . The right to left diagonal = . Their absolute difference is .

Function description

Complete the  function in the editor below. It must return an integer representing the absolute diagonal difference.

diagonalDifference takes the following parameter:

arr: an array of integers .
Input Format

The first line contains a single integer, , the number of rows and columns in the matrix .
Each of the next  lines describes a row, , and consists of  space-separated integers .

Constraints

Output Format

Print the absolute difference between the sums of the matrix's two diagonals as a single integer.

Sample Input

3
11 2 4
4 5 6
10 8 -12
Sample Output

15
Explanation

The primary diagonal is:

11
   5
     -12
Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10
Sum across the secondary diagonal: 4 + 5 + 10 = 19
Difference: |4 - 19| = 15

"""


def diagonalDifference(arr):
    result=0
    size=arr[0].__len__()
    if size == 1:
        return arr[0][0]*2
    for i in range(size):
        result+=arr[i][size-i-1]-arr[size-i-1][size-i-1]
    # for i in range(size):
    #     print(arr[size-i-1],arr[size-i-1][size-i-1])
    return abs(result)

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # n = int(input().strip())
    arr = [[1,2,3],
           [4,5,6],
           [9,8,9]]
    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()



