from .clsGlobalObject import *

class clsFileHandler:
    def __init__(self):
        globalObj=clsGlobal().get()
        self.path=globalObj["input_file_path"]
        pass

    def read_game_input(self):
        inputs=self.read_lines_from_file()
        lines=dict({
            "line1":inputs[0].split()
            ,"line2":int(inputs[1])
            ,"line3":inputs[2].split()
            ,"line4":inputs[3].split()
            ,"line5":inputs[4].split()
            ,"line6":inputs[5].split()
        })
        return lines

    def read_lines_from_file(self):
        lines=[]
        fileHandle = open(self.path, "r")
        for line in fileHandle:
            lines.append(line)
        return lines
