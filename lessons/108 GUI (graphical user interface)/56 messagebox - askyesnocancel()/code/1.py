from tkinter import *
from tkinter import messagebox

def klikle():
    # askyesnocancel() - bu metod 'yes', 'no', yaxud 'imtina' mesaji gosteren qutu yaratmaq ucundur.
    cavab = messagebox.askyesnocancel(title='Sual ver', message='Siz kodu sevirsiniz mi?')
    if(cavab == True):
        print("Beli")
    elif(cavab == False):
        print("Xeyr")
    else:
        print("Cavab vermekden imtina etdiniz")
    
    # yes dedikde    - True
    # no dedikde     - False
    # cancel dedikde - None deyerlerini elde edirik.
    
pencere = Tk()

duyme = Button(pencere, command=klikle, text="Duymeni bas")
duyme.pack()

pencere.mainloop()