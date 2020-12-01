from tkinter import mainloop
from tkinter.messagebox import showinfo
from oreilly.tkinter001 import MyGui

class CustomGui(MyGui):
    def reply(self):
        showinfo(title='popup', message='attached')
    #its been overriden as custom gui
    def onButtonClick(self):
        showinfo(title='popup', message='attached clicked overriden')

if __name__=='__main__':
    CustomGui().pack()
    mainloop()
