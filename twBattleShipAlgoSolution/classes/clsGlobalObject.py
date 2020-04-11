from .clsPlayers import *
from .clsConst import *


class clsGlobal:
    def __init__(self):
        pass

    def get(self):
        constObj=clsConst()
        return {
            "boardRowStart": 65
            , "players": clsPlayers().get()
            , "const": constObj.get()
            , "const_vars": constObj
            ,"input_file_path":"./gameInput.txt"
        }
