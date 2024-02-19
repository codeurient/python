from tkinter import *

pencere = Tk()

# command=    - duymeni basdiqda hansisa bir emeliyyat etmek ucun istifade edilen parametrdir.

def basmaq():
    print("Sen duymeni basdin")

# Diqqet etmelisiz ki, funksiyanin adini "command=" parametrine verdikde, funksiyanin adinin qarşısında () moterize qoymuruq. 
etiket = Button(
        pencere, 
        text="Duymeni bas!",
        command=basmaq
    )

etiket.pack()

pencere.mainloop()