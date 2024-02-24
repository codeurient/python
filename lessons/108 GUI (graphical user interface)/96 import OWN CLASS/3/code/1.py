from tkinter import *
from VoleybolTopu import *
import time

pencere = Tk()
WIDTH = HEIGHT = 500
canvas = Canvas(pencere, width=WIDTH, height=HEIGHT)
canvas.pack()

voleybol_topu = VoleybolTopu(canvas, 0, 0, 100, 1, 1, "white")

#! 1
# while ne qeder ki True-dur, pencere, update() metodu ile yenilenir ve her defe
# yenilendiyinde x ve y oxlari 1px deyeri artirlar. 
while True:
    voleybol_topu.hereket()
    pencere.update()
    time.sleep(.001)

pencere.mainloop()  