# Define a class which has at least two methods:
#     getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

class inputOutStringTest:
    def __init__(self):
        print("constructor is called")
        self.str1=""
    def method1(self):
        self.str1=input("enter some text\n")
    def method2(self):
        print("method1 called", self.str1.upper())

sObj=inputOutStringTest()
sObj.method1()
sObj.method2()