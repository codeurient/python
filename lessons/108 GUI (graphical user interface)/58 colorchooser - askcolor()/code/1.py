from tkinter import *
from tkinter import colorchooser

# 1) colorchooser modulunun askcolor() metodundan istifade ederek reng secmemize imkan saglayan pencereni yaradiriq
# 2) hemin metodu funksiya icinde yaziriq ve ele edirik ki, hemin pencere biz duymeni basdiqda acilsin.
def rengSec():
    # 3) reng adinda variable yaradaraq elde etdiyimiz rengi hemin variable-a veririk.
    reng = colorchooser.askcolor()
    # 4) reng variable-indaki deyeri terminal pencereye yazdiririq.
    # 5) Rengi, 2 deyer olaraq hem 'rgb' hemde 'hex' formatinda elde edirik. HEX formatinda olan rengi cagirmaq ucun []
    # kvadrat moterize istifade etmek lazimdir. rgb-i rengin indeksi 0 (sifir), hex-in indeksi ise 1-dir.
    print(reng)

    hexRengi = reng[1]
    print(hexRengi)

    # 6) 'config()' metodu icinde 'bg=' parametrine hemin rengi verdikde ve duymeni basdiqda acilmis olan pencere-nin arxa fon rengine 
    # bizim teyin etdiyimiz reng teyin edilecekdir.
    pencere.config(bg=hexRengi)

pencere = Tk()
pencere.geometry('420x420')
duyme = Button(text='Duymeni bas', command=rengSec)
duyme.pack()
pencere.mainloop() 