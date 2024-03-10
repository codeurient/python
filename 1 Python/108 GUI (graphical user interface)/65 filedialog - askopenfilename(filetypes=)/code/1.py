from tkinter import *
from tkinter import filedialog

def achmaq():
    # filetypes=  - bu parametr vasitesi ile sececeyimiz faylin novlerini teyin ede bilerik
    # Bu parametr emeliyyat sistemine gore ferqlilik gostere biler.
    faylinYolu = filedialog.askopenfilename(initialdir='lessons/108 GUI (graphical user interface)/62 filedialog - askopenfilename() - 2',
                                            title='Senedi acmaq istediyinizden eminsinizmi ?',
                                            filetypes=(
                                                ("text fayllari", "*.txt"),
                                                ("Diger fayllar", "*.*"),
                                            )
                                            )
    fayl = open(faylinYolu, 'r')
    print(  fayl.read()  )
    fayl.close()

pencere = Tk()

duyme = Button(text='Aç', command=achmaq)
duyme.pack()

pencere.mainloop() 