class io:
    def __init__(self, path):
        self.path = path
        print("the path is: ", path)

    def read(self, fileName):
        self.fileName = fileName
        self.fullPath = self.path + "\\" + self.fileName
        print("reading file", self.fullPath)
        print("The file contents are")
        f = open(self.fullPath)
        while True:
            line = f.readline()
            if len(line) == 0:
                break
            print(line)
        # close loop
        f.close

    def write(self, fileName, mode):
        self.mode = mode
        self.fileName = fileName
        self.fullPath = self.path + "\\" + self.fileName
        print("writting file", self.fullPath)
        poem = "Programming is fun\nWhen the work is done\nif you wanna make your work also fun"
        f = open(self.fullPath, mode)
        f.write(poem)
        f.close()
        print("The file has been written")
        # class end

        # io=io("F:\\corpTraininig\\python")
        # io.read("abc.txt")
        # io.write("testPy.txt","a")

        # mode: r, w, a, b
