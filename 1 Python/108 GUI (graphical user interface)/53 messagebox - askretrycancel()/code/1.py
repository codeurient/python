from tkinter import *
from tkinter import messagebox

def klikle():
    # askretrycancel() - bu metod 'imtina' ve 'yeniden cehd etmek' mesaji gosteren qutu yaratmaq ucundur.
    if messagebox.askretrycancel(title='Imtina & Yeniden cehd', message='Bunu etmek istediyinizden eminsiniz mi?'):
        print('Qebul etdiniz')
    else:
         print('Imtina etdiniz')

pencere = Tk()

duyme = Button(pencere, command=klikle, text="Duymeni bas")
duyme.pack()

pencere.mainloop()