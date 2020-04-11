import sys
import os
import copy


# qtype ships will be down in 2 hits, so keep their hit count * 2
# keep the hit counter -1 reducing and keep track of total hits becoming 0
# hits should be initialised by the ships counting position, on every missile launch, if its hits p or q, reduce it -1
def startGame(print_on_screen):
    gameInput = clsGameInput()
    objectInputValues = gameInput.take_game_input_from_text_file(print_on_screen)
    VALIDATED=constObject.VALIDATED
    if print_on_screen:
        print("validation object",objectInputValues)

    if (objectInputValues["line1_"+VALIDATED]
            and objectInputValues["line2_"+VALIDATED]
            and objectInputValues["line3_"+VALIDATED]
            and objectInputValues["line4_"+VALIDATED]
    ):
        boardObj = clsPlayerBoard()
        objBoardForPlayers = boardObj.generateBoardForPlayers(objectInputValues)
        # this is just to have shallow and deep copy funda (byVal or byRef, default is byRef ie. shallow
        updatedBoard = boardObj.placementOfShipsOnBoards(copy.deepcopy(objBoardForPlayers), objectInputValues)
        if print_on_screen:
            clsPrint().printPlayerBoard(updatedBoard)

        missiles = clsMissiles(print_on_screen)
        players[constObject.playerACounter], players[constObject.playerBCounter] = updatedBoard[constObject.playerACounter], updatedBoard[constObject.playerBCounter]
        result = missiles.launchMissiles(updatedBoard, objectInputValues)

        print("Final Position", result)
        if int(result[constObject.game_result][ players[constObject.playerAKey]+"sum" ])>0 and int(result[constObject.game_result][ players[constObject.playerBKey]+"sum" ])>0:
            print("games ends in DRAW, NO ONE WINS")
        else:
            print("game end. Thanks for playing.")

    else:
        print("there is some error in input values, please correct and restart. See log below for details.",
              objectInputValues[constObject.MSG])


if __name__ == '__main__':
    curpath=os.path.abspath(os.path.join(__file__,"../.."))
    print("appending to pythonpath",curpath)
    sys.path.append(curpath) #managing pythonpath, curfile execution has to be relative to path

    from classes.clsGameInput import *
    from classes.clsMissiles import *
    from classes.clsPlayerBoard import *
    from classes.clsPrint import *

    gameName = "game started - Battle Shield - War of Ships"
    globalObj = clsGlobal().get()
    constObject = globalObj["const_vars"]
    players = globalObj["players"]

    # arg_1="print=1" if sys.argv.__len__()==0 else sys.argv[1]
    arg_1="print=1"
    print_on_screen=int(str(arg_1).split('=')[1])
    print(gameName)
    startGame(print_on_screen)


