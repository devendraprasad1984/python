"""
Implement a GUI for viewing and updating class instances stored in a shelve; the shelve lives on the machine this script runs on,
as 1 or more local files;
"""

from tkinter import *
from tkinter.messagebox import showinfo, showwarning, showerror
import shelve

shelvename='class-people-shelve'
fieldNames=('name','age','job','pay')

def makeWidgets():
    global entries
    window=Tk()
    window.title('People Shelve Object')
    form=Frame(window)
    form.pack()
    entries={}
    formFields=('key',)+fieldNames
    for (ix,label) in enumerate(formFields):
        lab=Label(form,text=label)
        ent=Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label]=ent
    Button(window, text='Fetch', command=fetchRecord).pack(side=LEFT)
    Button(window, text='Update', command=updateRecord).pack(side=LEFT)
    Button(window, text='Quit', command=window.quit).pack(side=RIGHT)
    return window

def fetchRecord():
    # print(entries)
    key=entries['key'].get() #get from textbox id by key
    try:
        record=db[key]
    except:
        showerror(title='Error', message='no record found')
    else:
        for fld in fieldNames:
            entries[fld].delete(0, END)
            entries[fld].insert(0, repr(getattr(record, fld)))

def updateRecord():
    key=entries['key'].get() #get from textbox id by key
    if key in db:
        record=db[key]
    else:
        from oreilly.person import Person
        record=Person(name='?', age='?')
    for fld in fieldNames:
        setattr(record, fld, eval(entries[fld].get()))
    db[key]=record
    showinfo(title='update',message='record has been updated')


db=shelve.open(shelvename)
window=makeWidgets()
window.mainloop()
db.close() #back here if quit or window lose

