from .clsHelpFunctions import *
from .clsGlobalObject import *

class clsPlayerBoard:
    def __init__(self):
        globalObj=clsGlobal().get()
        constObj=globalObj["const_vars"]
        players=globalObj["players"]
        self.playerAName = players[constObj.playerAKey]
        self.playerBName = players[constObj.playerBKey]
        self.playerACounterObject = players[constObj.playerACounter]
        self.playerBCounterObject = players[constObj.playerBCounter]
        self.P_TYPE_HIT_COUNT = constObj.P_TYPE_HIT_COUNT
        self.Q_TYPE_HIT_COUNT = constObj.Q_TYPE_HIT_COUNT
        self.HIT = constObj.HIT
        self.MISS = constObj.MISS
        self.constObj=constObj
        return


    def updateBoardWithShip(self,boards, width, height, updateWithChar, placementIndexes):
        updatedBoard = boards
        # print(updatedBoard,width,height,placementIndexes)
        playerAPos, playerBPos = placementIndexes[self.playerAName], placementIndexes[self.playerBName]
        # updating position of width (cols of array) of board array
        for i_cell in range(width):
            updatedBoard[self.playerAName][playerAPos[0]][i_cell + playerAPos[1]] = updateWithChar
            updatedBoard[self.playerBName][playerBPos[0]][i_cell + playerBPos[1]] = updateWithChar

        # updating position of height (rows of array) of board array if height>1 as =1 is already covered above
        if height > 1:
            for i_cell in range(height):
                updatedBoard[self.playerAName][i_cell + playerAPos[0]][playerAPos[1]] = updateWithChar
                updatedBoard[self.playerBName][i_cell + playerBPos[0]][playerBPos[1]] = updateWithChar

        return updatedBoard


    def placementOfShipsOnBoards(self,boards, inputObject):
        q_type_dims_coords = inputObject["line3"]
        p_type_dims_coords = inputObject["line4"]

        q_type_width = int(q_type_dims_coords[1])
        q_type_height = int(q_type_dims_coords[2])
        q_type_pos_player1 = q_type_dims_coords[3]
        q_type_pos_player2 = q_type_dims_coords[4]

        p_type_width = int(p_type_dims_coords[1])
        p_type_height = int(p_type_dims_coords[2])
        p_type_pos_player1 = p_type_dims_coords[3]
        p_type_pos_player2 = p_type_dims_coords[4]

        # print("converted qtype positions and coords",q_type_dims_coords, q_type_width, q_type_height, getXY(q_type_pos_player1),getXY(q_type_pos_player2))
        # players Q type object counter initialization
        p_area=int(p_type_width) * int(p_type_height)
        q_area=2 * int(q_type_width) * int(q_type_height)
        self.playerACounterObject[self.P_TYPE_HIT_COUNT] = p_area
        self.playerACounterObject[self.Q_TYPE_HIT_COUNT] = q_area
        self.playerBCounterObject[self.P_TYPE_HIT_COUNT] = p_area
        self.playerBCounterObject[self.Q_TYPE_HIT_COUNT] = q_area

        # getting actual x,y coordinates with the 2d board array
        helpFunc=clsHelperFunctions()
        Q_playerXYPlacementIndex = {self.playerAName: helpFunc.getXY(q_type_pos_player1), self.playerBName: helpFunc.getXY(q_type_pos_player2)}
        P_playerXYPlacementIndex = {self.playerAName: helpFunc.getXY(p_type_pos_player1), self.playerBName: helpFunc.getXY(p_type_pos_player2)}

        # use here the width and height counters respectively for each player and place Q/P in specified cells starting from cellRef as given in input
        # updating board with placements of P/Q types ships
        boards = self.updateBoardWithShip(boards, q_type_width, q_type_height, "Q", Q_playerXYPlacementIndex)
        boards = self.updateBoardWithShip(boards, p_type_width, p_type_height, "P", P_playerXYPlacementIndex)
        boards[self.constObj.playerACounter]=self.playerACounterObject
        boards[self.constObj.playerBCounter]=self.playerBCounterObject
        # print("updating board placing ships",boards)
        print("ships are placed and are ready to attack")
        return boards


    def generateBoardForPlayers(self,inputObject):
        print("board generating...")
        widthAndHeightOfBattleArea, numOfBattleShips = inputObject["line1"], inputObject["line2"]
        helpFunc=clsHelperFunctions()
        boardColumns, boardRows = int(widthAndHeightOfBattleArea[0]), int(helpFunc.getBoardRowIndex(widthAndHeightOfBattleArea[1]))
        # boardColumns, boardRows = int(widthAndHeightOfBattleArea[0]), int(helpFunc.getBoardRowIndex('E'))
        # print("board rows & cols", boardRows, boardColumns)

        # playerACounterObject[TOTAL_SHIPS] = numOfBattleShips
        # playerBCounterObject[TOTAL_SHIPS] = numOfBattleShips

        # use generators here to generate the board with all 0 initially indicating blank cells where ships will be placed later as show in sample below
        board1 = [[0 for row in range(boardRows + 1)] for col in range(boardColumns)]
        board2 = [[0 for row in range(boardRows + 1)] for col in range(boardColumns)]
        print("player zones are ready")
        return {self.playerAName: board1, self.playerBName: board2}
