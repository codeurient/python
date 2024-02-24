from tkinter import *

pencere = Tk()

canvas = Canvas(pencere, height=500, width=500)
# create_polygon - bu metoddan coxbucaqli yaratmaq ucun istifade edilir.
# hal hazirda ucbucaqli yaratdiq. Koordinatlari list icine qoyaraqda istifade etmek mumkundur.

# outline - bu parametr ile xettin kenarlarinin rengini teyin eetmek mumkundur.
noqteler = [250, 0, 500, 500, 0, 500]
canvas.create_polygon(noqteler, fill="yellow", outline="black")
canvas.pack()

pencere.mainloop()  