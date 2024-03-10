from tkinter import *
from tkinter import filedialog

def yaddasaYaz():
    # 1) asksaveasfile() - bu metodan fayllari yaddasa yazmaq ucun istifade edilen pencerenin yaradilmasinda istifade edirik.

    # a) defaultextension - bu parametr ile yaddasa yazilacaq faylin varsayilan olaraq ".txt" formatinda olmasini deyirik. 

    # b) filetypes - bu parametr vasitesi ile DIGER format novlerinin ne ola bileceyini teyin edirik. Yeni, Secim sunuruq istifadeciye ki,
    # eger isteyirse format olaraq .txt evezine .html fomratinida secerek fayli yaddasa yaza biler.

    # c) initialdir - bu parametr ile, penceere acildiqda faylin bir basa cari senedin icinde yaddasa yazilmasini teyin edirik.
    #   Eger bu parametr olmasa pencere bize DESKTOP yeni fayli ANA EKRANA yaddasa yazmagi teklif edecekdir.
    fayl = filedialog.asksaveasfile(
                                    initialdir="lessons/108 GUI (graphical user interface)/65 filedialog - asksaveasfile()",
                                    defaultextension='.txt', 
                                    filetypes=[
                                        ("Text fayli",    ".txt"),
                                        ("HTML fayli",    ".html"),
                                        ("Diger fayllar", ".*"),
                                    ])
    # 2) Sahede yazdigimiz metni 'get()' metodu ile elde edirik.
    faylMetni = str(  metn.get(1.0, END)  )
    # 3) Elde etdiyimiz metni write() metodu ile acilan pencerenin komekliyi vasitesi ile komputerin yaddasina yaziriq.
    fayl.write(faylMetni)
    # 4) Yaddasa yazdiqdan sonra fayli baglayiriq.
    fayl.close()

pencere = Tk()

duyme = Button(text='Yaddasa yaz', command=yaddasaYaz)
duyme.pack()

metn = Text(pencere)
metn.pack()

pencere.mainloop() 