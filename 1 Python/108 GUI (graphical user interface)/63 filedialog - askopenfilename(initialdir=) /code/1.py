from tkinter import *
from tkinter import filedialog

def achmaq():
    # initialdir=  - 'Aç' sozune basdiqda hal-hazirda icinde oldugumuz qovlugun acilmasini isteyirikse onda, 
    # bu atributdan istifade edirik.

    # Mac ve Windows emeliyyat sistemlerinden asili olaraq ferqlilik gostere biler bu xususiyyet.
    # Yeni 'initialdir=' parametri olmadan da 'Aç' sozune basdiqda eger MAC emeliyyat sistemidise yenede cari sened acila biler.
    faylinYolu = filedialog.askopenfilename(initialdir='lessons/108 GUI (graphical user interface)/62 filedialog - askopenfilename() - 2')
    fayl = open(faylinYolu, 'r')
    print(  fayl.read()  )
    fayl.close()

pencere = Tk()

duyme = Button(text='Aç', command=achmaq)
duyme.pack()

pencere.mainloop() 