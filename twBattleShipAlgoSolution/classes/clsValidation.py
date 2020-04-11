class clsInputValidation():
    def __init__(self, inputObjectOfAllLines):
        self.inputObjectOfAllLines = inputObjectOfAllLines
        self.msgVar = "\nERROR MESSAGE IN INPUT"

        self.shipTypes = ['P', 'Q']
        self.inputline1 = self.inputObjectOfAllLines["line1"]
        self.inputline2 = self.inputObjectOfAllLines["line2"]
        self.inputline3 = self.inputObjectOfAllLines["line3"]
        self.inputline4 = self.inputObjectOfAllLines["line4"]
        self.inputline5 = self.inputObjectOfAllLines["line5"]
        self.inputline6 = self.inputObjectOfAllLines["line6"]

        self.widthOfBattleship = int(self.inputline1[0])
        self.heightOfBattleship = (int(ord(self.inputline1[1].__str__())) - 65 + 1)
        self.areaOfBattleships = self.widthOfBattleship * self.heightOfBattleship
        pass

    def validate_first_line(self):
        valid = True
        checkline = self.inputline1
        self.msgVar += "\nLine1: " + str(checkline)
        if (int(checkline[0]) <1 or int(checkline[0]) > 9):
            self.msgVar += "=>width of battle area out of range (1-9)"
            valid = False
        if (int(ord(checkline[1].__str__()))<65 or  int(ord(checkline[1].__str__())) > 90):
            self.msgVar += "=>height of battle area out of range (A-Z)"
            valid = False

        return valid

    def validate_second_line(self):
        valid = True
        checkline = self.inputline2
        self.msgVar += "\nLine2: " + str(checkline)
        if (int(checkline)<1 or int(checkline) > self.areaOfBattleships):
            self.msgVar += "=>area of battleships is range (M*N): " + self.areaOfBattleships.__str__()
            valid = False
        return valid

    def validate_third_line(self):
        return self.__checkLine3And4(self.inputline3)

    def validate_fourth_line(self):
        return self.__checkLine3And4(self.inputline4)

    # private method
    def __checkLine3And4(self, checkline):
        valid = True
        self.msgVar += "\nLine3: " + str(checkline)
        # print("contains check:",(checkline[0] in self.shipTypes))
        if (checkline[0] not in self.shipTypes):
            self.msgVar += "=>type of ship, valid types: " + self.shipTypes.__str__()
            valid = False
        # elif False == ((1 <= int(checkline[1]) <= self.widthOfBattleship) or (1 <= checkline[3] <= self.widthOfBattleship)): 3,4 need to be converted back to integer position and check
        if ((int(checkline[1]) <1 or  int(checkline[1]) > self.widthOfBattleship)):
            self.msgVar += "=>type of ship, valid width: " + self.widthOfBattleship.__str__()
            valid = False
        if ((int(checkline[2])<1 or int(checkline[2]) > self.heightOfBattleship)):
            self.msgVar += "=>type of ship, valid height: " + self.heightOfBattleship.__str__()
            valid = False

        return valid
