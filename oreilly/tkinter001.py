from tkinter import *
from tkinter.messagebox import showinfo

class MyGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        button=Button(self,text='click',command=self.onButtonClick)
        button.pack()
    def onButtonClick(self):
        showinfo('pop up','button pressed')

if __name__=='__main__':
    window=MyGui()
    window.pack()
    window.mainloop()

