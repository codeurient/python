from tkinter import *
from VoleybolTopu import *
import time

pencere = Tk()
WIDTH = HEIGHT = 500
canvas = Canvas(pencere, width=WIDTH, height=HEIGHT)
canvas.pack()

voleybol_topu = VoleybolTopu(canvas, 0, 0, 100, 1, 1, "white")

while True:
    voleybol_topu.hereket()
    pencere.update()
    time.sleep(1)

pencere.mainloop()  