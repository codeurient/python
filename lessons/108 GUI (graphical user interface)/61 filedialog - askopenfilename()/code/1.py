from tkinter import *
from tkinter import filedialog

# filedialog - bu modul fayllari acmaq ucun istifade edilen metodlari bize verir. 
# askopenfilename() - hemin metodlardan biri budur. Secmis oldugumuz faylin yolunu elde etmek ucun istifade edilir.
def achmaq():
    faylinYolu = filedialog.askopenfilename()
    print(faylinYolu)

pencere = Tk()


duyme = Button(text='Aç', command=achmaq)
duyme.pack()

pencere.mainloop() 