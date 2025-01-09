from tkinter import *
from tkinter import messagebox

def klikle():
    # showerror() - bu metod xeta mesaji gosteren pencere acmaq ucun istifade edilir.
    messagebox.showerror(title='Xeta', message='Bir xeta var')

pencere = Tk()

duyme = Button(pencere, command=klikle, text="Duymeni bas")
duyme.pack()

pencere.mainloop()