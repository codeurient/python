from tkinter import *

pencere = Tk()

siyahiQutusu = Listbox( pencere )
siyahiQutusu.pack()

# insert() - siyahi qutusunun icine elementler elave etmek ucun insert() metodundan istifade edirik.
siyahiQutusu.insert(  1, 'pizza'   )
siyahiQutusu.insert(  2, 'corek'   )
siyahiQutusu.insert(  3, 'sup'     )
siyahiQutusu.insert(  4, 'soyutma' )
siyahiQutusu.insert(  5, 'tike'    )

pencere.mainloop()