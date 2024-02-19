from tkinter import *

def gonder():
    ad = qeyd.get()
    print("salam: " + ad)
   
def silmek():
    qeyd.delete(0, END)

def tekTekSilmek():
    qeyd.delete(len(qeyd.get())-1, END)
    
pencere = Tk()

qeyd = Entry( pencere, font=('Arial', 30) )
# insert() metodu metn sahesine varsayilan deyer elave etmek ucun istifade edilir. 2 arqument qebul edir.
# 1ci arqument 0 baslangic pozisiyani teyin edir.
# 2ci arqument varsayilan deyer.
qeyd.insert(0, 'Varsayilan deyer')
qeyd.pack(side=LEFT)

gonderen_duyme = Button( pencere, text="Gonder", command=gonder )
gonderen_duyme.pack(side=RIGHT)

silen_duyme = Button( pencere, text="Sil", command=silmek )
silen_duyme.pack(side=RIGHT)

tekTekSilen_duyme = Button( pencere, text="Tek-tek sil", command=tekTekSilmek )
tekTekSilen_duyme.pack(side=RIGHT)

pencere.mainloop()