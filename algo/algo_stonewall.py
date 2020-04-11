# """
# Cover "Manhattan skyline" using the minimum number of rectangles.
# You are going to build a stone wall. The wall should be straight and N meters long, and its thickness should be constant; however, it should have different heights in different places. The height of the wall is specified by an array H of N positive integers. H[I] is the height of the wall from I to I+1 meters to the right of its left end. In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.
# The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular). Your task is to compute the minimum number of blocks needed to build the wall.
# Write a function:
# def solution(H)
# that, given an array H of N positive integers specifying the height of the wall, returns the minimum number of blocks needed to build it.
# For example, given array H containing N = 9 integers:
#   H[0] = 8    H[1] = 8    H[2] = 5
#   H[3] = 7    H[4] = 9    H[5] = 8
#   H[6] = 7    H[7] = 4    H[8] = 8
# the function should return 7. The figure shows one possible arrangement of seven blocks.
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..100,000];
# each element of array H is an integer within the range [1..1,000,000,000].
# """
def solution(H):
    stack = []
    block_count = 0    # The number of needing blocks
    for height in H:
        while len(stack) != 0 and height < stack[-1]:
            # If the height of current block is less than the previous ones, the previous ones have to end before current point. They have no chance to exist in the remaining part. So the previous blocks are completely finished.
            stack.pop()
            block_count += 1
        if len(stack) == 0 or height > stack[-1]:
            # If the height of current block is greater than the previous one, a new block is needed for current position.
            stack.append(height)
        # Else (the height of current block is same as that of previous one), they should be combined to one block.
    # Some blocks with different heights are still in the stack.
    block_count += len(stack)
    return block_count

H=[8,8,5,7,9,8,7,4,8]
print(solution(H))

