from tkinter import *
import time
pencere = Tk()
# WIDTH ve HEIGHT adlarinda 2 variable yaradaraq onlara 500 ededini deyer olaraq veririk.
WIDTH = HEIGHT = 500
xKoordinatininSureti = 2  # bu variable-llara baslangic deyer 1 veririk ki, sonradan bir-bir artirib bir-bir azaltmaq ucun istifade edek.
yKoordinatininSureti = 2  # bu variable-llara baslangic deyer 1 veririk ki, sonradan bir-bir artirib bir-bir azaltmaq ucun istifade edek.

canvas = Canvas(pencere, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

arxaFonSekli = PhotoImage(file="lessons/108 GUI (graphical user interface)/95 width(), height(), coords()/code/space.png")
arxaFon = canvas.create_image(0,0, image=arxaFonSekli, anchor=NW)

ufoSekli = PhotoImage(file="lessons/108 GUI (graphical user interface)/95 width(), height(), coords()/code/ufo.png")
# Burda ki, 0 (sifirlar) evez edilir, xKoordinatininSureti ve yKoordinatininSureti variable-larinin aldiqlari deyerleri ile.
sekil = canvas.create_image(0,0, image=ufoSekli, anchor=NW)

seklin_genisliyi = ufoSekli.width()     # width()  - bu metod ile seklin genislik  olcusunu elde edirik
seklin_hundurluyu = ufoSekli.height()   # height() - bu metod ile seklin hundurluk olcusunu elde edirik
while True:
    # coords() - bu metotdan, elementin hansi koordinatlarda yerlesdiyini oyrenmek ucun istifade edilir.
    koordinatlar = canvas.coords(sekil)
    # coords() metodu ile sekil adli variable-in icinden x ve y koordinatlarini aldiqdan sonra hemin koordinatlari basqa variable-a oturduk
    # bu variabel-in adini da 'koordinatlar' qoymusuq. Indi ise [] kvadrat moterizenin komekliyi ile hemin variable-a muraciet ede, hemcinin
    # 0 ve 1 indekslerinden faylanaraq, ayri-ayri bu koordinatlari elde ede bilerik: print(koordinatlar[0])
    #! (WIDTH - seklin_genisliyi) - bu o demekdir ki, sekil ekran genisliyinin kenarina cixmasin. 
    if(koordinatlar[0] >= (WIDTH - seklin_genisliyi) or koordinatlar[0] < 0):
        # Ilk once x oxunun deyeri arta arta gedir ve 380 beraber olduqda 380-ne, -1 ededi verilir 1-in ustune.
        # -1 bu sefer cixa-cixa gedir ve 0 (sifira) catdiqda 0-1= -1 edir. xKoordinatininSureti variable-i olur -1.
        # -1 ededine -1 verdikde musbet 1 elde edirik ve yeniden arta-arta getmeye baslayir x oxu. 
        xKoordinatininSureti = -xKoordinatininSureti
    #! (WIDTH - seklin_hundurluyu) - bu o demekdir ki, sekil ekran hundurluyunun kenarina cixmasin. 
    if(koordinatlar[1] >= (HEIGHT - seklin_hundurluyu) or koordinatlar[1] < 0):
        yKoordinatininSureti = -yKoordinatininSureti
    # move() - bu metod pencerede yerlesen obyekti (sekli) x=1, y=1 px qeder hereket etdirir. Hereketin daimi dovur vurmasi ucun While
    # konstruktorundan istifade etmisik. While True oldugu muddetce move() metod 1px, x ve y xolari boyunca sekli hereket etdirecekdir.
    canvas.move(sekil, xKoordinatininSureti, yKoordinatininSureti)
    # update() bu metotdan, her yeni bas veren deyiskliyi gormek ucun istifade edilir.
    pencere.update()
    time.sleep(0.001)
pencere.mainloop()  