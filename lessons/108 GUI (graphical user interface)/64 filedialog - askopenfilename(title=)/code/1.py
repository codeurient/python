from tkinter import *
from tkinter import filedialog

def achmaq():
    # title=  - bu parametrden acilan pencerenin basliq metnini deyisdirmek ucun istifade edilir.
    faylinYolu = filedialog.askopenfilename(initialdir='lessons/108 GUI (graphical user interface)/62 filedialog - askopenfilename() - 2',
                                            title='Senedi acmaq istediyinizden eminsinizmi ?')
    fayl = open(faylinYolu, 'r')
    print(  fayl.read()  )
    fayl.close()

pencere = Tk()

duyme = Button(text='Aç', command=achmaq)
duyme.pack()

pencere.mainloop() 