from .clsConst import *


class clsPlayers:
    A_P_Counter=0
    A_Q_Counter=0
    B_P_Counter=0
    B_Q_Counter=0

    def __init__(self):
        pass

    # implement observer design pattern on counter variables of players for ships hit/miss count
    @classmethod
    def get(myinstance):
        # constObject = clsConst().get()
        constObject = clsConst()
        playerAName, playerBName = "Player A", "Player B"

        #this indicates how many hits did playerA did on playerB
        playerACounterObject = {constObject.P_TYPE_HIT_COUNT: myinstance.A_P_Counter, constObject.Q_TYPE_HIT_COUNT: myinstance.A_Q_Counter}

        #this indicates how many hits did playerB did on playerA
        playerBCounterObject = {constObject.P_TYPE_HIT_COUNT: myinstance.B_P_Counter, constObject.Q_TYPE_HIT_COUNT: myinstance.B_Q_Counter}

        return {
            constObject.playerAKey: playerAName
            , constObject.playerBKey: playerBName
            , constObject.playerACounter: playerACounterObject
            , constObject.playerBCounter: playerBCounterObject
        }
