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

metn = Text(pencere)
metn.pack()

pencere.mainloop() 