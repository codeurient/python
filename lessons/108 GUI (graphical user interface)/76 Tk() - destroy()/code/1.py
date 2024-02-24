from tkinter import *

def yeniPencereYarat():
    yeni_pencere = Tk()
    # destroy() - duymeni basaraq yeni pencere yaratdiqda kohnesi avtomatik olaraq baglansin deye bu metodan istifade edilir.
    kohne_pencere.destroy()

kohne_pencere = Tk()

Button(kohne_pencere, text="Yeni pencere yaratmaq", command=yeniPencereYarat).pack()

kohne_pencere.mainloop()  