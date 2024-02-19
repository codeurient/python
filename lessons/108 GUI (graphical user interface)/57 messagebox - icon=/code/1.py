from tkinter import *
from tkinter import messagebox

def klikle():
    # icon=   - bu parametr ile var sayilan icon formasini deyismek mumkundur.
    cavab = messagebox.askyesnocancel(title='Sual ver', message='Siz kodu sevirsiniz mi?', icon='warning')
    if(cavab == True):
        print("Beli")
    elif(cavab == False):
        print("Xeyr")
    else:
        print("Cavab vermekden imtina etdiniz")
    
pencere = Tk()

duyme = Button(pencere, command=klikle, text="Duymeni bas")
duyme.pack()

pencere.mainloop()