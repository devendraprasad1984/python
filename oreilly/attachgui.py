from tkinter import *
from oreilly.tkinter001 import *

mainWin=Tk()
Label(mainWin, text=__name__).pack()

popup=Toplevel()
Label(popup, text='Attach').pack(side=LEFT)

MyGui(popup).pack(side=RIGHT)
mainWin.mainloop()
