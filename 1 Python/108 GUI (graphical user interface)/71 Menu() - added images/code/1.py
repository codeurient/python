from tkinter import *
from tkinter import filedialog

def fayliAc():
        faylinYolu = filedialog.askopenfilename(initialdir='lessons/108 GUI (graphical user interface)/62 filedialog - askopenfilename() - 2')
        fayl = open(faylinYolu, 'r')
        print(  fayl.read()  )
        fayl.close()
        
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

acmaqSekli = PhotoImage(file="1 Python/108 GUI (graphical user interface)/71 Menu() - added images/code/acmaq.png")
yaddaSaxlaSekli = PhotoImage(file="1 Python/108 GUI (graphical user interface)/71 Menu() - added images/code/cixis.png")
cixisEtSekli = PhotoImage(file="1 Python/108 GUI (graphical user interface)/71 Menu() - added images/code/yaddasaxla.png")

menuBar = Menu(pencere)
pencere.config(menu=menuBar)

fileMenu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_cascade(label="Open folder", command=fayliAc, image=acmaqSekli, compound=LEFT)
fileMenu.add_cascade(label="Yadda saxla", command=yaddaSaxla, image=yaddaSaxlaSekli, compound=LEFT)
fileMenu.add_separator()
fileMenu.add_cascade(label="Cix", command=cixisEt, image=cixisEtSekli, compound=LEFT)


redakteEt = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Redakte et", menu=redakteEt)
redakteEt.add_cascade(label="Kes", command=kesmek)
redakteEt.add_cascade(label="Kopyala", command=kopyalamaq)
redakteEt.add_cascade(label="Yapisdir", command=yapisdirmaq)

pencere.mainloop()  