# FIFO - first in first out
from collections import deque

queue = deque(["rohan", "sameer", "adil", "saksham"])
print(queue)

queue.append("priya")
queue.append("aashi")
print(queue)

delVal = queue.popleft()
print("the deleted value from queue is: " + delVal)
# queue.pop()
print(queue)
