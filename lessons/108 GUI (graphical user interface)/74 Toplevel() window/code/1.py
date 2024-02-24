from tkinter import *

def yeniPencereYarat():
    # Toplevel() - bu klasdan istifade ederek yeni pencere yaratdiqda: 
    # a) Eger yeni yaradilan pencereni baglasaq onda kohne pencere aciq qalacaq yeni pencere baglanacaq.
    # b) Eger yeni yaradilan pencere evezine kohne pencereni baglasaq onda hem yeni hem kohne pencere baglanacaq.
    yeni_pencere = Toplevel()

kohne_pencere = Tk()

Button(kohne_pencere, text="Yeni pencere yaratmaq", command=yeniPencereYarat).pack()

kohne_pencere.mainloop()  