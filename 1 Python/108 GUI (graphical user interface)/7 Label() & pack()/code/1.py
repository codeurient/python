from tkinter import *


pencere = Tk()




# Label() - bu klass 'tkinter' modulunun klasidir. 
# Bu klas ile, metnler, fontlar, sekiller, rengler hazirlamaq olur 
#! Label() klasi 2 parametr qebul edir: 
#? 1ci parametr pencere
#? 2ci parametr hemin pecnereye yerlesdirilecek etiket-dir.

etiket = Label(pencere, text="GUI derslerimize xos gelmisiz")

# pack() - Hazirladigimiz etiketleri pencereye yerlesdirmek ucun pack() metodundan istifade edilir.
#? pack() metodunun "side=" adinda parametri var ve bu parametrin deyerleri ile elementleri sol, sag hereket etdirmek olur
#? Bu hereket etdirme haqqinda olan numune 21ci qovlugun icinde olan 2ci qovluqda qeyd edilmisdir.
etiket.pack()


pencere.mainloop()