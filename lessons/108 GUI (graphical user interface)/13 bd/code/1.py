from tkinter import *

pencere = Tk()

# bd=10 - çərçivənin qalinligini teyin edir.

etiket = Label(
    pencere, 
    text="GUI derslerimize xos gelmisiz", 
    font=('Arial', 40, 'bold'), 
    fg='#00FF00', 
    bg='#BBBFFF',
    relief=RAISED,
    bd=10)

etiket.pack()

pencere.mainloop()