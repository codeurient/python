from tkinter import *

def gonder():
    print("Sifarisiniz:", siyahiQutusu.get(  siyahiQutusu.curselection()  ))

def elaveEt():
    siyahiQutusu.insert(  siyahiQutusu.size(), sahe.get()  )
    siyahiQutusu.config(height=siyahiQutusu.size())

def silmek():
    siyahiQutusu.delete(  siyahiQutusu.curselection()  )
    siyahiQutusu.config(height=siyahiQutusu.size())

pencere = Tk()
#! selectmode=   -  eger birden cox elementi eyni vaxtda secmek isteyirikse, onda bu parametrden istifade edirik.
# bes birden cox element secdikde onlari nece gondere yaxud sile bilerik ? 
siyahiQutusu = Listbox( pencere, selectmode=MULTIPLE )
siyahiQutusu.pack()

siyahiQutusu.insert(  1, 'pizza'   )
siyahiQutusu.insert(  2, 'corek'   )
siyahiQutusu.insert(  3, 'sup'     )
siyahiQutusu.insert(  4, 'soyutma' )
siyahiQutusu.insert(  5, 'tike'    )

siyahiQutusu.config(height=siyahiQutusu.size())

sahe = Entry()
sahe.pack()

gonder = Button(pencere, text='Gonder', command=gonder)
gonder.pack()

elaveEt = Button(pencere, text='Elave et', command=elaveEt)
elaveEt.pack()

sil = Button(pencere, text='Sil', command=silmek)
sil.pack()

pencere.mainloop()