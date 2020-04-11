from .clsGlobalObject import *
from .clsValidation import *
from .clsFileHander import *

class clsGameInput:
    def __init__(self):
        globalObj=clsGlobal().get()
        self.VALIDATED=globalObj["const_vars"].VALIDATED
        self.MSG=globalObj["const_vars"].MSG
        pass


    def take_game_input_from_text_file(self,print_on_screen):
        # there will be 6 lines in the file
        # this function name is just to check pep8 naming convension style
        """
            Input:
            The first line of the input contains the width and height of the battle area respectively.
            The second line of the input contains the number of battleships that each player gets.The third line of the input contains the type of the battleship, its dimensions (width and height) and coordinates for
            Player-1 and Player-2.
            The fourth line of the input contains the type of the battleship, its dimensions (width and height) and coordinates for
            Player-2 and Player-2.
            The fifth line contains the sequence of the target locations of missiles fired by Player-1.
            The sixth line contains the sequence of the target locations of missiles fired by Player-2.
        """
        # generate board from here and pass it to the main program for further dealing with the game
        # validate the input as per input conditions using a validate class
        inputlines=clsFileHandler().read_game_input()
        inputlines[self.VALIDATED]=True
        inputlines[self.MSG]=""
        if print_on_screen:
            print("input values are", inputlines)
        # use of shallow copy of object to be reflected back in calling routine for quick updates from a different function
        self.validateInput(inputlines)
        return inputlines


    def take_game_input(self):
        inputlines = dict(
            {"line1": "", "line2": "", "line3": "", "line4": "", "line5": "", "line6": "", self.MSG: ""})
        inputlines["line1"] = "5 E".split()
        inputlines["line2"] = "2"
        inputlines["line3"] = "Q 1 1 A1 B2".split()
        inputlines["line4"] = "P 2 1 D4 C3".split()
        inputlines["line5"] = "A1 B2 B2 B3".split()
        inputlines["line6"] = "A1 B2 B3 A1 D1 E1 D4 D4 D5 D5".split()
        print("input values are", inputlines)
        # use of shallow copy of object to be reflected back in calling routine for quick updates from a different function
        self.validateInput(inputlines)
        return inputlines

    def validateInput(self,inputlines):
        validate = clsInputValidation(inputlines)
        VALIDATED=self.VALIDATED
        inputlines["line1_"+VALIDATED] = validate.validate_first_line()
        inputlines["line2_"+VALIDATED] = validate.validate_second_line()
        inputlines["line3_"+VALIDATED] = validate.validate_third_line()
        inputlines["line4_"+VALIDATED] = validate.validate_fourth_line()
        inputlines[self.MSG] = validate.msgVar
        return
