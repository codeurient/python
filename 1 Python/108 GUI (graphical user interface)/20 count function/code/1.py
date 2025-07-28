from tkinter import *
from tkmacosx import *

# Her duymeni basdiqda say artiran funksiya yaratdiq. LIKE sistemine benzeyir.
say = 0
def basmaq():
    global say 
    say += 1
    print(say)

pencere = Tk()

sekil = PhotoImage(file='1 Python/108 GUI (graphical user interface)/20 count function/code/1.png')

etiket = Button(
        pencere, 
        text="Duymeni bas!",
        command=basmaq,
        fg="#00FF00",
        bg="#000",
        activeforeground="#00FF00",
        activebackground="#000",
        image=sekil,
        compound='bottom'
    )

etiket.pack()

pencere.mainloop()