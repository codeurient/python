from tkinter import *
from tkinter import colorchooser

def rengSec():
    # 58-ci dersde yazdigimiz kodu tek setr formasinda da yazmaq olardi.
    pencere.config(bg=colorchooser.askcolor()[1])

pencere = Tk()
pencere.geometry('420x420')
duyme = Button(text='Duymeni bas', command=rengSec)
duyme.pack()
pencere.mainloop() 