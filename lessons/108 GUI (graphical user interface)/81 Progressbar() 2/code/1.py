import time
from tkinter import *
from tkinter.ttk import *

def basla():
    tapsiriq = 100
    x = 0
    # 'x' ne qeder ki, kicikdir '100'-den x-in deyeri 'x+=1' (bir-bir) artsin. x-in deyeri 100 olduqda while dongusu
    # FALSE qaytaracaqdir ve dongu sonlanacaqdir. 
    while(x < tapsiriq):
        # while dongsu 0.03 saniye araliq ile isleyecekdir.
        time.sleep(.03)
        # Bu muddet erzinde Yuklenme Zolaginin yavas-yavas artigini goreceyik.
        yuklenmeZolagi['value'] += 1
        # Burda x-in deyerini bir-bir artiririq.
        x += 1
        #! update_idletasks() - Bu metod, proqram uzun emeliyyatlar icra etdikde istifadeci interfeysini yenileyir.
        #! while dongusu islediyi muddet boyunca update_idletasks() metodu goruntunu yeniliye-yenilye duracaqdir ki,
        #! her defe bas veren yeni deyisiklikleri gore bilek. 
        pencere.update_idletasks()

pencere = Tk()

yuklenmeZolagi = Progressbar(pencere, orient=HORIZONTAL, length=300)
yuklenmeZolagi.pack(pady=20)

duyme = Button(pencere, text="yuklenir", command=basla).pack()

pencere.mainloop()  