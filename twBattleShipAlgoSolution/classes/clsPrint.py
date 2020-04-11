from .clsGlobalObject import *

class clsPrint:
    def __init__(self):
        globalObj=clsGlobal().get()
        constObj=globalObj["const_vars"]
        self.playerAName=globalObj[constObj.playersKey][constObj.playerAKey]
        self.playerBName=globalObj[constObj.playersKey][constObj.playerBKey]
        self.chrRowStart=globalObj["boardRowStart"]
        self.constObj=constObj



    def printPlayerBoard(self,boardArrayObject):
        print("printing player(s) board")
        # print('\n'.join('{}: {}'.format(*k) for k in enumerate(boardArrayObject)))
        boardColsCount=len(boardArrayObject[self.playerAName][0])
        for (playerName, boardObject) in boardArrayObject.items():
            rowCounter = 0
            print("board and counter object for", playerName)

            if playerName==self.playerAName or playerName==self.playerBName:
                print('\t', end=' ')
                for col in range(boardColsCount):
                    print(col,end=' ')
                print('')
                for board in boardObject:
                    print(chr(self.chrRowStart + rowCounter), board)
                    rowCounter += 1

