from tkinter import *
from VoleybolTopu import *

pencere = Tk()
# 1) pencerede canvas sahesini yaratdiq. Genisliyi ve Hundurluyu 500 px teyin etdik.
WIDTH = HEIGHT = 500
canvas = Canvas(pencere, width=WIDTH, height=HEIGHT)
canvas.pack()

# 2) VoleybolTopu.py dokumenti icinde hemin adda CLASS yaratdiq ve bu faylin icine import ederek cagirdiq.
voleybol_topu = VoleybolTopu(canvas, 0, 0, 100, 1, 1, "white")

pencere.mainloop()  