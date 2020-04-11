class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    # raise MyError("logging has the issue")
    print("multiply operation: " + str(2 * 2 * 2))
    print("deivide operation: " + str(10 / 2))
    raise MyError("divide by 0 has come")
except MyError as e:
    print('user defined exception has occured:' + e.value)
