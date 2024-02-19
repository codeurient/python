from tkinter import *
from tkinter import filedialog

def yaddasaYaz():
    fayl = filedialog.asksaveasfile(
                                    initialdir="lessons/108 GUI (graphical user interface)/65 filedialog - asksaveasfile()",
                                    defaultextension='.txt', 
                                    filetypes=[
                                        ("Text fayli",    ".txt"),
                                        ("HTML fayli",    ".html"),
                                        ("Diger fayllar", ".*"),
                                    ])
    # fayli yaddasa yazmayaraq IMTINA (cancel) duymesini basdiqda xeta mesaji aliriq:
    #!  AttributeError: 'NoneType' object has no attribute 'write'
    # if - is sorgusu ile hemin xeta mesajinin qarsini ala bilerik. Yeni, Eger secilmis fayl yoxdursa, return et deyirik. 
    # Niye tekce 'return' yazdiq ? return False yaxud True yox ? Cunki deyer vermeden sadece 'return' yazmaq sadece funksiyanin
    # işini dayandırmaq üçün istifadə edilən qaydadır. Burdakı, meqsed funksiyanin dəyər qaytarması deyildir, sadəcə işi dayandırmasıdır.
    if fayl is None:
        return
        
    faylMetni = str(  metn.get(1.0, END)  )
    fayl.write(faylMetni)
    fayl.close()

pencere = Tk()

duyme = Button(text='Yaddasa yaz', command=yaddasaYaz)
duyme.pack()

metn = Text(pencere)
metn.pack()

pencere.mainloop() 