from .clsRowResolver import *
from .clsGlobalObject import *

class clsHelperFunctions:
    def __init__(self):
        globalObj = clsGlobal().get()
        self.chrRowStart = globalObj["boardRowStart"]
        self.resolver = clsRowResolver()

    def getBoardRowIndex(self, charValue):
        numRow = self.resolver.getRowRef(charValue) - self.chrRowStart
        return numRow

    def getXY(self, cellPositionRef):
        if cellPositionRef=='x':
            print('all options are drained, correct input and try again')
            return False
        xy = [0, 0]
        # getting x,y integer from cell ref, e.g. A1=0,0,D4=(3,3) as board index is starting from 0,0
        xy[0], xy[1] = int(self.getBoardRowIndex(cellPositionRef[0:1])), int(cellPositionRef[1:]) - 1
        return xy
