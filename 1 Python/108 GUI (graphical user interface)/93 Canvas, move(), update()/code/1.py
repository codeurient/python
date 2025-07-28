from tkinter import *

#! 2 
# move() - bu metod Canvas icindeki obyektdi hereket etdirmek ucun istifade edilir. 
# 1ci parametr hereket etdirelecek obyektdir. 
# 2ci parametr x oxudur.
# 3cu parametr y oxudur.
def yuxari_hereket(event):
    canvas.move(sekil, 0, -10) #! x oxu deyismez qalir, y oxunu 10 azaldiriq

def asagi_hereket(event):
    canvas.move(sekil, 0, 10) #! x oxu deyismez qalir, y oxunu 10 artiririq 

def sola_hereket(event):
    canvas.move(sekil, -10, 0) #! x oxunu 10 azaldiriq, y oxu deyismez qalir

def saga_hereket(event):
    canvas.move(sekil, 10, 0) #! x oxunu 10 artiririq, y oxu deyismez qalir

#! 1 
pencere = Tk()

pencere.bind("<w>", yuxari_hereket)
pencere.bind("<s>", asagi_hereket)
pencere.bind("<a>", sola_hereket)
pencere.bind("<d>", saga_hereket)

canvas = Canvas(pencere, width=500, height=500)
canvas.pack()

masinSekli = PhotoImage(file='1 Python/108 GUI (graphical user interface)/93 Canvas, move(), update()/code/racecar.png')

# create_image() bu metod 'canvas' icinde sekil yerlesdirmek ucun istifade edilir. 
# '1ci ve 2ci' parametrler seklin hansi koordinatlarda yerleseceyini teyin edir. '3cu' parametri hansi seklin olacagini teyin edir. 
# anchor=  - '4cu' parametr ise seklin canvas qutusunun tam sol ve yuxari yerinde yerleseceyini teyin edir.
sekil = canvas.create_image(0, 0, image=masinSekli, anchor=NW)

pencere.mainloop()  