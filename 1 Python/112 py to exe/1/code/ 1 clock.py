# Windows sistemlerinde proqrami ise saldiqda antivirus proqramlari yaxud defender proqramin işə salınmasını
# engelleye biler. Ilk once hemin antivirus ve defender proqramlarini qapadin. 

# Proqrami hazirlamaga baslamadan evvel bu iki komandani yazmagi unutmayin:
# 1) pip install --upgrade pip
# 2) pip install --upgrade pyinstaller

# 1) Ana ekranda clock adinda bir qovluq yaradiriq. Qovlugun adini 'clock' qoydum men.
# 2) Qovlugun icine 'png' formatinda bir sekil elave etdim ve adini bele qoydum: clock.png
    #! Ancaq bize uzantisi .png yox .ico lazimdir. Buunun ucun bu sayta kecid ederek png formatini ico formatina konvert edirik: https://icoconvert.com/ 
# Kodumuzun yerlesdiyi fayli da hemin qovlugun icine qoyuruq. Faylin adini men bele qoymusam: clock.py

# Indi ise terminal-da hemin qovluga kecid edirik:  #!    cd ~/Desktop/clock
# Sonra ise terminalda bu komandani yaziriq:        #!    pyinstaller -F -w -i clock.ico clock.py
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