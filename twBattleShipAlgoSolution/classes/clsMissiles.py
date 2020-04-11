from .clsHelpFunctions import *
from .clsGlobalObject import *

class clsMissiles:
    def __init__(self,print_on_screen):
        globalObj=clsGlobal().get()
        constObj=globalObj["const_vars"]
        self.print_on_screen=print_on_screen
        self.playerAName = globalObj[constObj.playersKey][constObj.playerAKey]
        self.playerBName = globalObj[constObj.playersKey][constObj.playerBKey]
        # playerACounterObject = globalObj["players"]["playerACounter"]
        # playerBCounterObject = globalObj["players"]["playerBCounter"]
        self.P_TYPE_HIT_COUNT = constObj.P_TYPE_HIT_COUNT
        self.Q_TYPE_HIT_COUNT = constObj.Q_TYPE_HIT_COUNT
        self.HIT= constObj.HIT
        self.MISS= constObj.MISS
        self.constObj=constObj


    def launchMissiles(self, boards, inputObject):
        helperFunc=clsHelperFunctions()
        print("launching missiles...")
        winnerAnnounced=False
        playerACounterObject,playerBCounterObject=boards[self.constObj.playerACounter],boards[self.constObj.playerBCounter]
        missiles_player1, missiles_player2 = inputObject["line5"], inputObject["line6"]

        if self.print_on_screen:
            print(self.playerAName, missiles_player1, len(missiles_player1))
            print(self.playerBName, missiles_player2, len(missiles_player2))

        maxMissileObject = missiles_player1 if (len(missiles_player1) >= len(missiles_player2)) else missiles_player2
        # loop over position of the largest array of the 2 and take respective values for player turns
        # at some point, the smallest index would be unavailable, handle that
        # decrease the hit counter in player object and check count continuously to announce winner who hits the other first i.e. make hitcounters (p+q) all 0
        player1MissileTargets = ['x'] * len(maxMissileObject)
        player2MissileTargets = ['x'] * len(maxMissileObject)
        # generate missile object with equla number of elements
        for i in range(len(maxMissileObject)):
            if i < len(missiles_player1): player1MissileTargets[i] = missiles_player1[i]
            if i < len(missiles_player2): player2MissileTargets[i] = missiles_player2[i]

        # launching from equal set of elements - now easy to keep track of target pos and check the x empty pos
        player1_missile_loop_counter = 0
        player2_missile_loop_counter = 0
        for pos in range(len(maxMissileObject)):
            while not winnerAnnounced:
                if player1_missile_loop_counter>=len(player1MissileTargets): break
                if player1MissileTargets[player1_missile_loop_counter] != 'x':
                    if playerACounterObject[self.P_TYPE_HIT_COUNT] + playerACounterObject[self.Q_TYPE_HIT_COUNT] <= 0:
                        print(self.playerAName, "wins and thus ends the game - WINNER")
                        winnerAnnounced=True
                        break

                    xy = helperFunc.getXY(player1MissileTargets[player1_missile_loop_counter])
                    x, y = xy[0], xy[1]
                    cellValue = boards[self.playerBName][x][y] #opponent striked
                    if cellValue == 'Q' and playerACounterObject[self.Q_TYPE_HIT_COUNT]>0: playerACounterObject[self.Q_TYPE_HIT_COUNT] -= 1
                    if cellValue == 'P' and playerACounterObject[self.P_TYPE_HIT_COUNT]>0: playerACounterObject[self.P_TYPE_HIT_COUNT] -= 1
                    # A will target B locations and vice versa
                    print(self.playerAName, "takes chance and fires missile at ",
                          player1MissileTargets[player1_missile_loop_counter], "and gets", cellValue, "which means its",
                          (self.HIT if cellValue != 0 else self.MISS))
                    player1_missile_loop_counter += 1
                    if cellValue == 0: break
                else:
                    print(self.playerAName, "has left no missiles")
                    break

            while not winnerAnnounced:
                if player2_missile_loop_counter>=len(player2MissileTargets): break
                if player2MissileTargets[player2_missile_loop_counter] != 'x':
                    if playerBCounterObject[self.P_TYPE_HIT_COUNT] + playerBCounterObject[self.Q_TYPE_HIT_COUNT] <= 0:
                        print(self.playerBName, "wins and thus ends the game - WINNER")
                        winnerAnnounced=True
                        break

                    xy = helperFunc.getXY(player2MissileTargets[player2_missile_loop_counter])
                    x, y = xy[0], xy[1]
                    cellValue = boards[self.playerAName][x][y] #opponent striked
                    if cellValue == 'Q' and playerBCounterObject[self.Q_TYPE_HIT_COUNT]>0: playerBCounterObject[self.Q_TYPE_HIT_COUNT] -= 1
                    if cellValue == 'P' and playerBCounterObject[self.P_TYPE_HIT_COUNT]>0: playerBCounterObject[self.P_TYPE_HIT_COUNT] -= 1
                    # B will target A locations and vice versa
                    print(self.playerBName, "takes chance and fires missile at ",
                          player2MissileTargets[player2_missile_loop_counter], "and gets", cellValue, "which means its",
                          (self.HIT if cellValue != 0 else self.MISS))
                    player2_missile_loop_counter += 1
                    if cellValue == 0: break
                else:
                    print(self.playerBName, "has left no missiles")
                    break
        # just the final counter of hits
        objResult = dict()
        objResult[self.constObj.game_result]=dict({
            self.playerAName:playerACounterObject
            ,self.playerBName:playerBCounterObject
            ,self.playerAName+"sum":playerACounterObject[self.P_TYPE_HIT_COUNT] + playerACounterObject[self.Q_TYPE_HIT_COUNT]
            ,self.playerBName+"sum":playerBCounterObject[self.P_TYPE_HIT_COUNT] + playerBCounterObject[self.Q_TYPE_HIT_COUNT]
        })
        return objResult
