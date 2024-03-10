from tkinter import *

# curselection() - bu metoddan, hal-hazirda siyahi qutusunda olan hansi elementi secmisikse onu elde 
#                  etmek ucun istifade edilir. 
def gonder():
    deyer = siyahiQutusu.get(  siyahiQutusu.curselection()  )
    print(deyer)

pencere = Tk()

siyahiQutusu = Listbox( pencere )
siyahiQutusu.pack()

siyahiQutusu.insert(  1, 'pizza'   )
siyahiQutusu.insert(  2, 'corek'   )
siyahiQutusu.insert(  3, 'sup'     )
siyahiQutusu.insert(  4, 'soyutma' )
siyahiQutusu.insert(  5, 'tike'    )

siyahiQutusu.config(height=siyahiQutusu.size())

gonder = Button(pencere, text='Gonder', command=gonder)
gonder.pack()

pencere.mainloop()