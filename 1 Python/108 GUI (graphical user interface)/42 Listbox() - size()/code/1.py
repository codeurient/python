from tkinter import *

pencere = Tk()

siyahiQutusu = Listbox( pencere )
siyahiQutusu.pack()

siyahiQutusu.insert(  1, 'pizza'   )
siyahiQutusu.insert(  2, 'corek'   )
siyahiQutusu.insert(  3, 'sup'     )
siyahiQutusu.insert(  4, 'soyutma' )
siyahiQutusu.insert(  5, 'tike'    )

# size() - bu metod config() metodunun icinde istifade edildikde, siyahi qutusunun hundurluyunu 
# hemin qutunun icinde olan elementlerin hundurluyune beraber edir.
siyahiQutusu.config(height=siyahiQutusu.size())

pencere.mainloop()