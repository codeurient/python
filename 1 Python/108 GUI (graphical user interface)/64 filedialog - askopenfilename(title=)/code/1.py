from tkinter import *
from tkinter import filedialog

def achmaq():
    # title=  - bu parametrden acilan pencerenin basliq metnini deyisdirmek ucun istifade edilir.
    faylinYolu = filedialog.askopenfilename(initialdir='1 Python/108 GUI (graphical user interface)/64 filedialog - askopenfilename(title=)',
                                            title='Senedi acmaq istediyinizden eminsinizmi ?')
    fayl = open(faylinYolu, 'r')
    print(  fayl.read()  )
    fayl.close()

pencere = Tk()

duyme = Button(text='Aç', command=achmaq)
duyme.pack()

pencere.mainloop() 