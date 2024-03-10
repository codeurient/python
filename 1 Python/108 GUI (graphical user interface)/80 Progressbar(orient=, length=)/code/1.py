from tkinter import *
from tkinter.ttk import *

def basla():
    # 4) Yuklenme zolaginin icindeki her defe artan deyer hemin zolagin deyeri sayilir. 
    # Bu deyeri elde etmek ucun ilk once [] kvadrat moterize ile yuklenme zolagina
    # muraciet edirik, sonra ise 'value' acari ile hemin deyeri cagiraraq on-on (10-10)
    # artiririq. Maksimum 100-e catmasi ucun 10 defe duymeni basdiqda 100 tamamlanacaqdir.
    #! Nece etmek olarki, duymeni 1 defe basdiqda yuklenme zolagi da 1 defeye yuklensin ? Bunun ucun 'while' 
    #! konstruktorundan istifade etmek mumkundur.  
    yuklenmeZolagi['value'] += 10

pencere = Tk()

# 1) Progressbar() klasi ile yuklenme zolagi yaradiriq. 
# 2) length= parametri yuklenme zolaginin uzunlugunu teyin edir.
yuklenmeZolagi = Progressbar(pencere, orient=HORIZONTAL, length=300)
yuklenmeZolagi.pack(pady=20)

# 3) Duymeni basdiqda yuklenme zolaginin yuklenmesi ucun yuxarida funksiya yaradiriq.
duyme = Button(pencere, text="yuklenir", command=basla).pack()

pencere.mainloop()  