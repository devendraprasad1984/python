"""
A small frog wants to get to the other side of the road. The frog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.
Count the minimal number of jumps that the small frog must perform to reach its target.
Write a function:
def solution(X, Y, D)
that, given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.
For example, given:
  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:
after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
Write an efficient algorithm for the following assumptions:
X, Y and D are integers within the range [1..1,000,000,000];
X ≤ Y.
"""

def solution(x,y,d):
    min_num_jump=float(0)
    new_x=float(x)
    while(new_x<float(y)):
        min_num_jump+=1
        new_x+=float(d)
        print(new_x)
    return min_num_jump

def solution2(X,Y,D):
    distance = Y - X
    if distance % D == 0:
        return distance//D
    else:
        return distance//D + 1

# min_jump=solution(10,85,30)
# min_jump=solution(3, 10000000, 7)
min_jump=solution2(3, 999111321, 7)
# min_jump=solution(3, 999111321, 2)
# min_jump=solution(3, 999111321, 99)
# min_jump=solution(3, 999111321, 1283)
print("min number of jump a frog will take is",min_jump)
