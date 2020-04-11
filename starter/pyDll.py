def SayHello():
    msg = "welcome to pytnon dll program!"
    return msg


def Add(a, b):
    return a + b


def Sub(a, b):
    return a - b


def Mult(a, b):
    return a * b


def Div(a, b):
    return a / b


def Mod(a, b):
    return a % b

# return SayHello()
# print(msg)

# command to convert python programm to dll
# goto the path from pyDll.py is residing and run following
# python -m py_compile pyDll.py



# from ctypes import *
# print windll.kernel32 # doctest: +WINDOWS
# print cdll.msvcrt # doctest: +WINDOWS
# libc = cdll.msvcrt # doctest: +WINDOWS
