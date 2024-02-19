from tkinter import *

pencere = Tk()

# pady=10 (padding y) - Y oxu istiqametinde, çərçivə ile yazi arasinda iç boşluq yaradır.

etiket = Label(
    pencere, 
    text="GUI derslerimize xos gelmisiz", 
    font=('Arial', 40, 'bold'), 
    fg='#00FF00', 
    bg='#BBBFFF',
    relief=RAISED,
    bd=10,
    padx=10,
    pady=25)

etiket.pack()

pencere.mainloop()