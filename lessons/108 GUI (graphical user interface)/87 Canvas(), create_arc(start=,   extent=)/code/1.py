from tkinter import *

pencere = Tk()

canvas = Canvas(pencere, height=500, width=500)
# 1) create_arc() - bu metod yay, yaxud dairenin yarisi, yaxud elips formasinda fiqurlar hazirlamaq ucun istifade edilir.

# 2) style= - create_arc() metodunun style= atributuna ferqli deyerler ferereq, ferqli formalar elde etmek mumkundur.
# meselen style=PIESLICE, style=CHORD, style=ARC ve.s

# 3) extent= - bu parametr dairenin neçə qradus açılması gərəkdiyini təyin edir.
canvas.create_arc(0,0,500,500, style=PIESLICE, start=20, extent=180)
canvas.pack()

pencere.mainloop()  