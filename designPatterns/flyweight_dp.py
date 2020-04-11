"""
Use sharing to support large numbers of fine-grained objects efficiently.
The Motif GUI strategy of replacing heavy-weight widgets with light-weight gadgets
Designing objects down to the lowest levels of system "granularity" provides optimal flexibility, but can be unacceptably expensive in terms of performance and memory usage.
ach "flyweight" object is divided into two pieces: the state-dependent (extrinsic) part, and the state-independent (intrinsic) part. Intrinsic state is stored (shared) in the Flyweight object. Extrinsic state is stored or computed by client objects, and passed to the Flyweight when its operations are invoked
Whereas Flyweight shows how to make lots of little objects, Facade shows how to make a single object represent an entire subsystem
Flyweight is often combined with Composite to implement shared leaf nodes.

"""
#Use sharing to support large numbers of fine-grained objects efficiently.
import abc
class FlyWeightFactory:
    """
    Create and manage flyweight objects.
    Ensure that flyweights are shared properly. When a client requests a
    flyweight, the FlyweightFactory object supplies an existing instance
    or creates one, if none exists.
    """
    def __init__(self,fw_obj):
        self._flyweights={}
        self._fw_obj=fw_obj
    def get_flyweight(self,key):
        try:
            fw=self._flyweights[key]
        except Exception:
            # fw=ConcreteFlyweight()
            fw=self._fw_obj
            self._flyweights[key]=fw
        return fw
    def getAllFW(self):
        for (i,v) in self._flyweights.items():
            print(i)
        pass
class Flyweight(metaclass=abc.ABCMeta):
    """
    Declare an interface through which flyweights can receive and act on
    extrinsic state.
    """
    def __init__(self):
        self.intrinsic_state=None
    @abc.abstractmethod
    def operation(self,extrinsic_state):
        pass
class xFlyweight(Flyweight):
    """Implement the Flyweight interface and add storage for intrinsic state, if any. A ConcreteFlyweight object must be sharable. Any state it stores must be intrinsic; that is, it must be independent of the ConcreteFlyweight object's context. """
    def operation(self, extrinsic_state):
        print("xFlyweight - operation",extrinsic_state)
class yFlyweight(Flyweight):
    def operation(self, extrinsic_state):
        print("yFlyweight - operation",extrinsic_state)
class zFlyweight(Flyweight):
    def operation(self, extrinsic_state):
        print("zFlyweight - operation",extrinsic_state)

def main():
    fw_factory=FlyWeightFactory(xFlyweight())
    concrete_fw=fw_factory.get_flyweight("key1")
    concrete_fw.operation({"stateX":"what an state","nameX":"cool dude"})
    concrete_fw.operation({"stateY":"what an state","nameY":"what bro"})

if __name__ == '__main__':
    main()
