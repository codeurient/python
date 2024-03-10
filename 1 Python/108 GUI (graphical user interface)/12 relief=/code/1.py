
from tkinter import *

pencere = Tk()

# relief=RAISED - çərçivə yaratmaq üçün istifadə edilir.
# RAISED deyeri cercivenin qabariq olmasi ucundur. 3D effekti yaratmaq ucun istifade edilir.

# relief=SUNKEN

etiket = Label(
    pencere, 
    text="GUI derslerimize xos gelmisiz", 
    font=('Arial', 40, 'bold'), 
    fg='#00FF00', 
    bg='#BBBFFF',
    relief=RAISED)

etiket.pack()

pencere.mainloop()