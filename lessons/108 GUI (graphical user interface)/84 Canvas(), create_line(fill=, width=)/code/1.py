from tkinter import *

pencere = Tk()

# 1) Canvas() klasi qrafikler, fiqurlar, sekiller cekmeye imkan yaradan vidjetdir.
canvas = Canvas(pencere, height=500, width=500)
# 2) create_line() - bu metod duz xett yaratmaq ucun istifade edilir.
# a) 1ci parametr X-in baslangic koordinatini teyin edir.   (sol yuxari kunc baslangicdir)
# a) 2ci parametr Y-in baslangic koordinatini teyin edir.   (sol yuxari kunc baslangicdir)
# a) 3cu parametr X-in bitis koordinatini teyin edir.       (sag asagi kunc bitisdir)
# a) 4cu parametr Y-in bitis koordinatini teyin edir.       (sag asagi kunc bitisdir)

# 3) fill atributu xettin rengini teyin edir. 
# 4) width parametri xettin qalinligini teyin edir.
canvas.create_line(0, 0, 500, 500, fill="blue", width=5)
canvas.pack()


pencere.mainloop()  