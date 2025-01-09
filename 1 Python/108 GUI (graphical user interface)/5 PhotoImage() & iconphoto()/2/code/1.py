from tkinter import *

pencere = Tk()

pencere.geometry("420x420")
pencere.title("Birinci GUI dersimiz")

# fayl ve sekil eyni qovluqda yerlesirler. Niye onda sadece "logo.png" yazmiriq ? Emeliyyat sistemine gore ola biler.
# Nece etsek bes qisaca sadece "logo.png" yaza bilerik ?
logo = PhotoImage(file="1 Python/108 GUI (graphical user interface)/5 PhotoImage() & iconphoto()/2/code/logo.png")

pencere.iconphoto(True, logo)

pencere.mainloop()