# Sonra ise terminalda bu komandani yaziriq:        #!    pyinstaller -F -w -i clock.ico clock.py
    #? -F               - her sey 1 faylin icinde olsun demekdir.
    #? -w               - is bitdikden sonra terminal pencereden cix demekdir.
    #? -i icon.ico      - ikonu proqrama elave et demekdir. (goruntu yaradiriq)
    #? clock.py         - hansi fayli proqrama ceviririkse onun adini yaziriq.


from tkinter import *
from time import *

def vaxti_yenile():
    vaxt_metni = strftime("%I:%M:%S")
    vaxt_etiketi.config(text=vaxt_metni)
    
    gun_metni = strftime("%A")
    gun_etiketi.config(text=gun_metni)

    tarix_metni = strftime("%B %d, %Y")
    tarix_etiketi.config(text=tarix_metni)

    vaxt_etiketi.after(1000, vaxti_yenile)

pencere = Tk()
vaxt_etiketi = Label(pencere, font=("Arial", 50), fg="#00FF00", bg="black")
vaxt_etiketi.pack()

gun_etiketi = Label(pencere, font=("Arial", 25))
gun_etiketi.pack()

tarix_etiketi = Label(pencere, font=("Arial", 30))
tarix_etiketi.pack()

vaxti_yenile()
pencere.mainloop()  