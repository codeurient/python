from tkinter import *
from VoleybolTopu import *
import time

pencere = Tk()
WIDTH = HEIGHT = 500
canvas = Canvas(pencere, width=WIDTH, height=HEIGHT)
canvas.pack()

voleybol_topu = VoleybolTopu(canvas, 0, 0, 100, 1, 1, "white")

#! proqramdan cixis etdikde bele bir xeta aliriq:  _tkinter.TclError: invalid command name ".!canvas"
# Cunki, proqrami qapadiriq ancaq sonsuz dongu icinde proqram qapanan vaxti yenede  update() metodu is gormeye calisir.
# 6 nomrede hemin xetanin aradan qaldirilmasini izah etmisem. 
while True:
    voleybol_topu.hereket()
    pencere.update()
    time.sleep(.001)

pencere.mainloop()  