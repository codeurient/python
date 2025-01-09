from tkinter import *
from tkinter import messagebox

def klikle():
    # showwarning() - bu metod xeberdarliq mesaji gosteren pencere acmaq ucun istifade edilir.
    messagebox.showwarning(title='Tehluke', message='Virus var')

pencere = Tk()

duyme = Button(pencere, command=klikle, text="Duymeni bas")
duyme.pack()

pencere.mainloop()