from tkinter import *

pencere = Tk()

canvas = Canvas(pencere, height=500, width=500)
canvas.create_arc(0,0,500,500, fill="red", extent=180, width=10, outline="black")
canvas.create_arc(0,0,500,500, fill="white", extent=180, start=180, width=10, outline="black")

# create_oval() - bu parametrden oval, dairevi ve.s kimi formalar yaratmaq ucun istifade edilir.
canvas.create_oval(190, 190, 310, 310, fill="white", width=10, outline="black")
canvas.pack()

pencere.mainloop()  