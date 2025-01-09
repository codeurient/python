from tkinter import *
from tkinter import messagebox

def klikle():
    # askokcancel() - bu metod 'ok' ve 'imtina' mesaji gosteren qutu yaratmaq ucundur.
    if messagebox.askokcancel(title='ok yaxud imtina', message='Bunu etmek istediyinizden eminsiniz mi?'):
        print('Qebul etdiniz')
    else:
         print('Imtina etdiniz')

pencere = Tk()

duyme = Button(pencere, command=klikle, text="Duymeni bas")
duyme.pack()

pencere.mainloop()