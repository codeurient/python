from tkinter import *

pencere = Tk()

menuBar = Menu(pencere)
pencere.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_cascade(label="Ac")
fileMenu.add_cascade(label="Yadda saxla")
# add_separator() - bu metod, yuxaridaki etiketler ile asagidaki etiketler arasinda duz xett cekerek onlari ayirmaq ucun istifade edilir.
fileMenu.add_separator()
fileMenu.add_cascade(label="Cix")

pencere.mainloop()  