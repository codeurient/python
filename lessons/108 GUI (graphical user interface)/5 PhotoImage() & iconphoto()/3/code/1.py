import os
from tkinter import *

# Hal hazirda hansi qovlugun icindeyikse hemin qovlugun adini elde edirik.
#! /Users/proj/domains/PYTHON/lessons/108 GUI (graphical user interface)/5 PhotoImage() & iconphoto()/3/code
current_directory = os.path.dirname(__file__)
# join() metodu "logo.png" sekline hemin yuxarida elde etdiyimiz yolun adini birlesdirir.
#! /Users/proj/domains/PYTHON/lessons/108 GUI (graphical user interface)/5 PhotoImage() & iconphoto()/3/code/logo.png
image_path = os.path.join(current_directory, "logo.png")



pencere = Tk()

pencere.geometry("420x420")
pencere.title("Birinci GUI dersimiz")

logo = PhotoImage(file=image_path)

pencere.iconphoto(True, logo)

pencere.mainloop()