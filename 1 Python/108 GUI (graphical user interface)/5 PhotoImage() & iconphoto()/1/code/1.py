from tkinter import *

pencere = Tk()

pencere.geometry("420x420")
pencere.title("Birinci GUI dersimiz")



# PhotoImage(), tkinter modulunun klasidir. Sekilleri fayllarin icinden yuklemek ucun istifade edilir.
logo = PhotoImage(file="/Users/proj/domains/PYTHON/1 Python/108 GUI (graphical user interface)/5 PhotoImage() & iconphoto()/1/code/logo.png")

# iconphoto(), tkintermodulunda ki, Tk klasinin metodudur.
# 2 atribut qebul edir.
# 1ci atribut True yaxud False ola biler. True olarsa sekil butun acilan pencerelerde gorsenecek. False olarsa sadece esasda.
# 2ci atribut icon kimi istifade edilecek sekildir.
pencere.iconphoto(True, logo)



pencere.mainloop()