from tkinter import *

pencere = Tk()

etiket = Label(pencere, text="GUI derslerimize xos gelmisiz")

# place() - bu metod ile yerlesdirdiyimiz etiketi "sag sol yuxari asagi" hereket etdire bilerik.
# 1ci parametr X oxudur
# 2ci parametr Y oxudur
etiket.place(x=0, y=0)

pencere.mainloop()