"""
Offer a significant performance boost; it is most effective in situations where the cost of initializing a class instance is high, the
rate of instantiation of a class is high, and the number of instantiations in use at any one time is low.
"""

class ReusablePool:
    #manage reusable object for clients
    def __init__(self,max_size=1):
        self._reusables=[Reusable() for _ in range(max_size)]
    def acquire(self):
        print("object acquired")
        return self._reusables.pop() #it would return back one Reusable object from the list and is out
    def release(self, reusable):
        print("release")
        self._reusables.append(reusable) #put object back in list
class Reusable:
    # Collaborate with other objects for a limited amount of time, then they are no longer needed for that collaboration
    def __init__(self):
        self.xobj="new x object"
        pass
    def processData(self, dbcon):
        print("data processed ",self.xobj)
        return "done"

def main():
    reusable_pool=ReusablePool(10)
    reusable_obj_from_pool=reusable_pool.acquire()
    reusable_obj_from_pool.processData("any object or data to work within processing")
    reusable_pool.release(reusable_obj_from_pool)

if __name__ == '__main__':
    main()
