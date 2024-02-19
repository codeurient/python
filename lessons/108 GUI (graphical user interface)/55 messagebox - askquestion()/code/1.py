from tkinter import *
from tkinter import messagebox

def klikle():
    # askquestion() - bu metod 'yes' ve 'no' mesaji gosteren qutu yaratmaq ucundur.
    cavab = messagebox.askquestion(title='Sual ver', message='Tort sevirsen mi?')
    if (cavab == 'yes'):
        print('Beli tort sevirem')
    else:
         print('Niye tort sevmirsen?')

pencere = Tk()

duyme = Button(pencere, command=klikle, text="Duymeni bas")
duyme.pack()

pencere.mainloop()