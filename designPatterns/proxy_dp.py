"""
Provide a surrogate or placeholder for another object to control access to it.
Use an extra level of indirection to support distributed, controlled, or intelligent access.
Add a wrapper and delegation to protect the real component from undue complexity
You need to support resource-hungry objects, and you do not want to instantiate such objects unless and until they are actually requested by the client
Design a surrogate, or proxy, object that: instantiates the real object the first time the client makes a request of the proxy, remembers the identity of this real object, and forwards the instigating request to this real object. Then all subsequent requests are simply forwarded directly to the encapsulated real object.
The Proxy provides a surrogate or place holder to provide access to an object. A check or bank draft is a proxy for funds in an account. A check can be used in place of cash for making purchases and ultimately controls access to cash in the issuer's account.
eg CNMS proxy server calls to CIL interfaces allowing all clients to deal with proxy only
Adapter provides a different interface to its subject. Proxy provides the same interface. Decorator provides an enhanced interface.
Decorator and Proxy have different purposes but similar structures. Both describe how to provide a level of indirection to another object, and the implementations keep a reference to the object to which they forward requests.

"""
"""
Provide a surrogate or placeholder for another object to control access
to it or add other responsibilities.
"""
import abc

class subject(metaclass=abc.ABCMeta):
    # Define the common interface for RealSubject and Proxy so that a proxy can be used anywhere a RealSubject is expected.
    @abc.abstractmethod
    def request(self):
        pass

class RealSubject(subject):
    #Define the real object that the proxy represents.
    def request(self):
        print("request now in real came from proxy object")

# Maintain a reference that lets the proxy access the real subject. Provide an interface identical to Subject's.
class Proxy(subject):
    def __init__(self, real_subject):
        self._real_subject=real_subject
    def request(self):
        self._real_subject.request()
        print("control back in now proxy")

def main():
    xreal=RealSubject()
    proxy=Proxy(xreal)
    proxy.request()


if __name__ == '__main__':
    main()
