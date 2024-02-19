from tkinter import *

def gonder():
    ad = qeyd.get()
    print("salam: " + ad)
    qeyd.config(state=DISABLED)

def silmek():
    qeyd.delete(0, END)

def tekTekSilmek():
    qeyd.delete(len(qeyd.get())-1, END)
    
pencere = Tk()

#! show="*" - SAHE-de yazilan her seyi ulduz simvolu kimi gostermek ucun istifade edilir.
qeyd = Entry( pencere, font=('Arial', 30), show="*" )
qeyd.pack(side=LEFT)

gonderen_duyme = Button( pencere, text="Gonder", command=gonder )
gonderen_duyme.pack(side=RIGHT)

silen_duyme = Button( pencere, text="Sil", command=silmek )
silen_duyme.pack(side=RIGHT)

tekTekSilen_duyme = Button( pencere, text="Tek-tek sil", command=tekTekSilmek )
tekTekSilen_duyme.pack(side=RIGHT)

pencere.mainloop()