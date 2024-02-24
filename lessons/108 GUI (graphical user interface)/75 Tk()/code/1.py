from tkinter import *

def yeniPencereYarat():
    # Tk() - bu klasdan istifade ederek yeni pencere yaratdiqda: 
    # a) Eger yeni yaradilan pencereni baglasaq kohne pencere yenede aciq qalacaq
    # b) Eger yeni yaradilan pencere evezine kohne pencereni baglasaq onda kohne pencere yene de aciq qalmaga devam edecek. 
    yeni_pencere = Tk()

kohne_pencere = Tk()

Button(kohne_pencere, text="Yeni pencere yaratmaq", command=yeniPencereYarat).pack()

kohne_pencere.mainloop()  