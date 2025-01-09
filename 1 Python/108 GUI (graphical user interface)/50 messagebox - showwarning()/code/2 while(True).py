from tkinter import *
from tkinter import messagebox

def klikle():
    # Sonsuz dongu yaradaraq hemin qutunu daima aciq saxlaya bilerik. 
    while True:
        messagebox.showwarning(title='Tehluke', message='Virus var')

pencere = Tk()

duyme = Button(pencere, command=klikle, text="Duymeni bas")
duyme.pack()

pencere.mainloop()