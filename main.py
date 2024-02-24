from tkinter import *
from time import *

def vaxti_yenile():
    vaxt_metni = strftime("%I:%M:%S")
    vaxt_etiketi.config(text=vaxt_metni)


pencere = Tk()
vaxt_etiketi = Label(pencere, font=("Arial", 50), fg="#00FF00", bg="black")
vaxt_etiketi.pack()

vaxti_yenile()

pencere.mainloop()  