if __name__ == '__main__':
    from starter.QueueClass import Queue
else:
    from .QueueClass import Queue


def hotPotato(namedList, iterations):
    print("element after",iterations,"iterations")
    qObj = Queue()
    for n in namedList:
        qObj.enqueue(n)
    print("we have these elements in queue",str(qObj.size()))
    while qObj.size() > 1:
        for j in range(iterations):
            elem=qObj.dequeue()
            qObj.enqueue(elem)
        qObj.dequeue()
    return qObj.dequeue()


def main():
    lstName = ['A', 'B', 'C', 'D', 'E', 'F']
    print(hotPotato(lstName, 10))


if __name__ == '__main__':
    main()
