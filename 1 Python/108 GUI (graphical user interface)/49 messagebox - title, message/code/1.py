from tkinter import *
from tkinter import messagebox

def klikle():
    # title=   - bu atribut ile qutuya basliq metni elave etmek olur
    # message= - bu atribut ile qutunun icine mesaj yazdirmaq olur.
    messagebox.showinfo(title='Bu info tertibli mesajdir', message='Sen duymeni basdin')

pencere = Tk()

duyme = Button(pencere, command=klikle, text="Duymeni bas")
duyme.pack()

pencere.mainloop()