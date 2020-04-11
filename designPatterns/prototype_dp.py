"""
Specify the kinds of objects to create using a prototypical instance,
and create new objects by copying this prototype.
"""
import copy

class prototype:
    #example class to be copied
    pass
def main():
    prototype=prototype()
    proto_copy=copy.deepcopy(prototype) #the whole object of that class has been copied onto a new object
    pass

if __name__ == '__main__':
    main()