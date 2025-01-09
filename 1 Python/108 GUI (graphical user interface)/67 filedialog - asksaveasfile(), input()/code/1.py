from tkinter import *
from tkinter import filedialog

def yaddasaYaz():
    fayl = filedialog.asksaveasfile(
                                    initialdir="1 Python/108 GUI (graphical user interface)/67 filedialog - asksaveasfile(), input()/code/numune.txt",
                                    defaultextension='.txt', 
                                    filetypes=[
                                        ("Text fayli",    ".txt"),
                                        ("HTML fayli",    ".html"),
                                        ("Diger fayllar", ".*"),
                                    ])
    #! faylMetni = str(  metn.get(1.0, END)  )
    # input() - Yuxarida gorduyunuz kod evezine input() metodundan da istifade ederek Metn elave ede bilerik.
    # Pencere acildiqda var olan bir fayli secmek lazimdir. Bu vaxti terminal pencerede input() metodu bizden bir seyler yazmagimizi
    # teleb edecekdir. Yazi yazdiqdan sonra ENTER duymesini basaraq hemin secmis oldugumuz faylin icine yazi yaza bilerik. Bu vaxti
    # kohne yazi silinecekdir.
    faylMetni = input("Bir metn daxil edin: ")
    fayl.write(faylMetni)
    fayl.close()

pencere = Tk()

duyme = Button(text='Yaddasa yaz', command=yaddasaYaz)
duyme.pack()


pencere.mainloop() 