class clsRowResolver():
    def __init__(self):
        pass

    @staticmethod
    def getRowRef(charvalue):
        arrayRowRef = ord(str(charvalue))  # getting ascii value
        # print("character value equivalent", charvalue, arrayRowRef)
        return arrayRowRef
