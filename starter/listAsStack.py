# LIFO - Last In First Out
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


s = Stack()
print("Stack by class example")
print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

# another simple form of list as stack
print("Exampe of list as stack")
stack = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(stack)
val = stack.pop()
print("Delete value is: " + str(val))
stack.append(20)
print(stack)
