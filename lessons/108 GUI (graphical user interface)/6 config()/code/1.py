import os
from tkinter import *

current_directory = os.path.dirname(__file__)
image_path = os.path.join(current_directory, "logo.png")


pencere = Tk()
pencere.geometry("420x420")
pencere.title("Birinci GUI dersimiz")
logo = PhotoImage(file=image_path)
pencere.iconphoto(True, logo)

# config() - bu metoddan pencerenin arxa fon rengini deyismek ucun istifade edilir.
# pencere.config(background="#2596be")  - Belede yazmaq olar
# pencere.config(background="red")      - Belede yazmaq olar
#!  https://imagecolorpicker.com/en
pencere.config(background="#2596be")


pencere.mainloop()