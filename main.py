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