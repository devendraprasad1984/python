"""
Control write access to class attributes, Separate data from methods that use it ,Encapsulate class data initialization, Providing new type of final - final after constructor
A class may have one-time mutable attributes that cannot be declared final. Using this design pattern allows one-time setting of those class attributes. The motivation for this design pattern comes from the design goal of protecting class state by minimizing the visibility of its attributes (data).
"""

class DataClass:
    #hide all attributes
    def __init__(self):
        self.value=None
    def __get__(self,instance,owner):
        return self.value
    def __set__(self, instance, value):
        if self.value is None:
            self.value=value

class mainClass:
    #init data class thru data classes constructor
    attr=DataClass()
    def __init__(self,value):
        self.attr=value
        print("inside main class",self.attr)

def main():
    m=mainClass(True)
    print(m.attr) #once set is always set throughout objects life
    m.attr=False
    print(m.attr)
    m.attr=True
    print(m.attr)


if __name__ == '__main__':
    main()