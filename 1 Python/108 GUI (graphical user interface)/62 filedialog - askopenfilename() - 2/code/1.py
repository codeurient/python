from tkinter import *
from tkinter import filedialog

def achmaq():
    faylinYolu = filedialog.askopenfilename()
    # open() - bu metod fayli acir. 1ci parametr faylin yolunu 2ci parametr acilan faylin formatini teyin edir. 'r' yeni sadece oxumaq ucun.
    fayl = open(faylinYolu, 'r')
    # read() - bu metod acilan faylin terkibini oxumaq ucun istifade edilir.
    print(  fayl.read()  )
    # close() - bu metod ise fayli acaraq terkibini oxuduqdan sonra qapatmaq ucun istifade edilir.
    fayl.close()


pencere = Tk()

duyme = Button(text='Aç', command=achmaq)
duyme.pack()

pencere.mainloop()