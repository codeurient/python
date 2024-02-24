from tkinter import *

pencere = Tk()

cercive = Frame(pencere, bg="pink", bd=5, relief=SUNKEN)
cercive.place(x=100, y=100)

Button(cercive, text="W", font=("Consolas", 25), width=3).pack(side=TOP)
Button(cercive, text="A", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(cercive, text="S", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(cercive, text="D", font=("Consolas", 25), width=3).pack(side=LEFT)

pencere.mainloop()  