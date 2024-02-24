from tkinter import *

def fayliAc():
    print("Fayl acildi")
def yaddaSaxla():
    print("Fayl yddasa yazildi")
def kesmek():
    print("Kesdiniz")
def kopyalamaq():
    print("Kopyaladiniz")
def yapisdirmaq():
    print("Yapisdirdiniz")

def cixisEt():
    pass

pencere = Tk()

acmaqSekli = PhotoImage(file="lessons/108 GUI (graphical user interface)/71 Menu() - added images/code/acmaq.png")
yaddaSaxlaSekli = PhotoImage(file="lessons/108 GUI (graphical user interface)/71 Menu() - added images/code/yaddasaxla.png")
cixisEtSekli = PhotoImage(file="lessons/108 GUI (graphical user interface)/71 Menu() - added images/code/cixis.png")

menuBar = Menu(pencere)
pencere.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_cascade(label="Ac", command=fayliAc, image=acmaqSekli, compound=LEFT)
fileMenu.add_cascade(label="Yadda saxla", command=yaddaSaxla, image=yaddaSaxlaSekli, compound=LEFT)
fileMenu.add_separator()
fileMenu.add_cascade(label="Cix", command=cixisEt, image=cixisEtSekli, compound=LEFT)


redakteEt = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Redakte et", menu=redakteEt)
redakteEt.add_cascade(label="Kes", command=kesmek)
redakteEt.add_cascade(label="Kopyala", command=kopyalamaq)
redakteEt.add_cascade(label="Yapisdir", command=yapisdirmaq)

pencere.mainloop()  