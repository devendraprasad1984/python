class clsConst:
    def __init__(self):
        self.TOTAL_SHIPS="totalships"
        self.P_TYPE_COUNT="ptypeCount"
        self.Q_TYPE_COUNT= "qtypeCount"
        self.P_TYPE_HIT_COUNT= "ptypeHitCount"
        self.Q_TYPE_HIT_COUNT= "qtypeHitCount"
        self.VALIDATED= "validated"
        self.HIT= "HIT"
        self.MISS= "MISS"
        self.MSG= "msg"
        self.playerACounter="playerACounter"
        self.playerBCounter="playerBCounter"
        self.playerAKey="playerAName"
        self.playerBKey="playerBName"
        self.playersKey="players"
        self.game_result="game_result"
        pass

    def get(self):
        # print("constants self",self)
        return {
            "TOTAL_SHIPS": "totalships"
            , "P_TYPE_COUNT": "ptypeCount"
            , "Q_TYPE_COUNT": "qtypeCount"
            , "P_TYPE_HIT_COUNT": "ptypeHitCount"
            , "Q_TYPE_HIT_COUNT": "qtypeHitCount"
            , "VALIDATED": "validated"
            , "HIT": "HIT"
            , "MISS": "MISS"
            , "MSG": "msg"
        }