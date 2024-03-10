from tkinter import *

def gonder():
    # Nə üçün 1 yaxud 0 (sifir) yazmadiq da 1.0 yazdiq? 
    # 1 -  mətnin birinci sətrinə işarə edir.
    # 0 -  mətnin birinci sətrindəki ilk simvola işarə edir.
    # END - ise sonsuz kimi qebul edile biler. Yeni ne qeder istesek o qeder yazi yaza bilerik.
    sahe = metn.get("1.0", END)
    print(sahe)

pencere = Tk()

metn = Text(pencere)
metn.pack()

duyme = Button(pencere, text='Gonder', command=gonder)
duyme.pack()

pencere.mainloop() 