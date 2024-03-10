from tkinter import *
from VoleybolTopu import *
import time

pencere = Tk()
WIDTH = HEIGHT = 500
canvas = Canvas(pencere, width=WIDTH, height=HEIGHT)
canvas.pack()

# Bir CLASS yazdiq ve sadece deyisen deyerler oldu. CLASS-lar gorduyumuz isleri dinamiklesdirmek ucun cox muhum rola sahibdirler.
voleybol_topu = VoleybolTopu(canvas, 0, 0, 100, 1, 1, "white")
tenis_topu = VoleybolTopu(canvas, 0, 0, 50, 4, 3, "yellow")
basketbol_topu = VoleybolTopu(canvas, 0, 0, 125, 8, 7, "orange")

try:
    # funksiya yaradiriq hansi ki, pencerenin qapali yaxud aciq oldugunu yoxlayir. 
    def yoxla_pencere_qapandimi():
        # winfo_exists() - bu metod vidjetin aciq yaxud qapali oldugunu sorgulayan metotdur. 
        # Ve eger qapali deyilse destroy() metodu ile vidjeti mehv edirik
        if not pencere.winfo_exists():
            pencere.destroy()
            # Vidjet mehv edildikden sonracc(yeni qapadildiqdan sonra) proqram artiq hecne etmesin deye sadece return yaziriq.
            return
        # Eks halda funksiya pencereni update() ede duracaqdir her 10 milli saniyeden bir. 
        # Bunun ucun yeni her 10 milli saniyeden bir funksiya, pencerenin aciq olub olmadigini yoxlasin deye 
        # after() metodundan istifade etmisik. Yeni, eger pencere qapandisa destroy() et qapanmadisa update() et.
        voleybol_topu.hereket()
        tenis_topu.hereket()
        basketbol_topu.hereket()
        pencere.update()
        pencere.after(10, yoxla_pencere_qapandimi)

    yoxla_pencere_qapandimi()
except TclError as e:
    print("Ошибка:", e)



pencere.mainloop()  