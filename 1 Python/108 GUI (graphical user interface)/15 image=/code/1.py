from tkinter import *

pencere = Tk()

# image=  - çərçivəyə şəkil əlavə etmək üçün istifade edilir.

# Bunun ucun ilk once sekli PhotoImage() klasi ile cagiririq.
sekil = PhotoImage(file="/Users/proj/domains/PYTHON/1 Python/108 GUI (graphical user interface)/15 image=/code/1.png")

etiket = Label(
    pencere, 
    text="GUI derslerimize xos gelmisiz", 
    font=('Arial', 40, 'bold'), 
    fg='#00FF00', 
    bg='#BBBFFF',
    relief=RAISED,
    bd=10,
    padx=10,
    pady=10,
    image=sekil)

etiket.pack()

pencere.mainloop()