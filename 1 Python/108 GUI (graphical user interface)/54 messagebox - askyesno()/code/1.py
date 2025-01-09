from tkinter import *
from tkinter import messagebox

def klikle():
    # askyesno() - bu metod 'yes' ve 'no' mesaji gosteren qutu yaratmaq ucundur.
    if messagebox.askyesno(title='Yes yaxud no', message='Tort sevirsen mi?'):
        print('Beli tort sevirem')
    else:
         print('Niye tort sevmirsen?')

pencere = Tk()

duyme = Button(pencere, command=klikle, text="Duymeni bas")
duyme.pack()

pencere.mainloop()