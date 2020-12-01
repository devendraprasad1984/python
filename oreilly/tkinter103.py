from tkinter import *
from tkinter.messagebox import showinfo


def reply(name):
    showinfo(title='reply', message='hello %s'% name)

top = Tk()
top.title('Echo')
top.iconbitmap('py-blue_trans_out.icon')

Label(top, text='Enter Your Name').pack(side=TOP)
name=Entry(top)
name.pack(side=TOP)

btn=Button(top, text='Submit', command=lambda : reply(name.get()))
btn.pack(side=LEFT)

top.mainloop()
