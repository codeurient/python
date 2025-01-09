from tkinter import *

pencere = Tk()

canvas = Canvas(pencere, height=500, width=500)
# create_rectangle - bu metoddan duzbucaqli yaratmaq ucun istifade edilir.
canvas.create_rectangle(50, 50, 250, 250, fill="blue")
canvas.pack()


pencere.mainloop()  