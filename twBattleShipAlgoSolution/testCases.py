# import pytest
import os, sys

# python -m pytest -v -s --capture=no testCases.py
# pytest -v -s --capture=no testCases.py
# pytest -v -s --capture=no classes/testCases.py
# python -m pytest -v classes/testCases.py
# pytest classes/testCases.py::test_char_getRowRef
# @pytest.fixture(scope="session")

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

# curpath=os.path.abspath(os.path.join(__file__,"../.."))
# print("curpath",curpath)
# sys.path.append(curpath) #managing pythonpath, curfile execution has to be relative to path


from .clsPlayerBoard import *
from .clsGameInput import *
from .clsPrint import *
from .clsRowResolver import *


def test_char_getRowRef():
    objRowResolver = clsRowResolver()
    assert (objRowResolver.getRowRef("A") == 65)
    # assert (objRowResolver.getRowRef("B") == 65)

def test_1_1():
    assert 1==1

def test_print_board():
    # just to test the placement of ships on console, whether they are ok in their cells or not
    print("test printing board")
    objectInputValues = clsGameInput().take_game_input_from_text_file(print_on_screen=1)
    boardObj = clsPlayerBoard()
    objBoardForPlayers = boardObj.generateBoardForPlayers(objectInputValues)
    updatedBoard = boardObj.placementOfShipsOnBoards(objBoardForPlayers, objectInputValues)
    clsPrint().printPlayerBoard(updatedBoard)
    assert (1 == 1)
