import os
from tkinter import *


current_directory = os.path.dirname(__file__)

image_path = os.path.join(current_directory, "logo.png")





pencere = Tk()

pencere.geometry("420x420")
pencere.title("Birinci GUI dersimiz")

logo = PhotoImage(file=image_path)

pencere.iconphoto(True, logo)

pencere.mainloop()


