from tkinter import *

def yuxari_hereket(event):
    # winfo_x() - bu metod SEKLIN pəncərənin sol kənarından ne qeder mesafede yerlesdiyini qaytarir. 
    # winfo_y() - bu metod SEKLIN pəncərənin yuxari sol kənarından ne qeder mesafede yerlesdiyini qaytarir. 
    etiket.place(x = etiket.winfo_x(), y = etiket.winfo_y() - 10) #! x oxu deyismez qalir, y oxunu 10 azaldiriq

def asagi_hereket(event):
    # winfo_x() - bu metod SEKLIN pəncərənin sol kənarından ne qeder mesafede yerlesdiyini qaytarir. 
    # winfo_y() - bu metod SEKLIN pəncərənin yuxari sol kənarından ne qeder mesafede yerlesdiyini qaytarir. 
    etiket.place(x = etiket.winfo_x(), y = etiket.winfo_y() + 10) #! x oxu deyismez qalir, y oxunu 10 artiririq 

def sola_hereket(event):
    # winfo_x() - bu metod SEKLIN pəncərənin sol kənarından ne qeder mesafede yerlesdiyini qaytarir. 
    # winfo_y() - bu metod SEKLIN pəncərənin yuxari sol kənarından ne qeder mesafede yerlesdiyini qaytarir. 
    etiket.place(x = etiket.winfo_x() - 10, y = etiket.winfo_y()) #! x oxunu 10 azaldiriq, y oxu deyismez qalir

def saga_hereket(event):
    # winfo_x() - bu metod SEKLIN pəncərənin sol kənarından ne qeder mesafede yerlesdiyini qaytarir. 
    # winfo_y() - bu metod SEKLIN pəncərənin yuxari sol kənarından ne qeder mesafede yerlesdiyini qaytarir. 
    etiket.place(x = etiket.winfo_x() + 10, y = etiket.winfo_y()) #! x oxunu 10 artiririq, y oxu deyismez qalir

pencere = Tk()
pencere.geometry("500x500")

pencere.bind("<w>", yuxari_hereket)
pencere.bind("<s>", asagi_hereket)
pencere.bind("<a>", sola_hereket)
pencere.bind("<d>", saga_hereket)
pencere.bind("<Up>", yuxari_hereket)
pencere.bind("<Down>", asagi_hereket)
pencere.bind("<Left>", sola_hereket)
pencere.bind("<Right>", saga_hereket)

masinSekli = PhotoImage(file='1 Python/108 GUI (graphical user interface)/92 racecar/code/racecar.png')
etiket = Label(pencere, image=masinSekli)
etiket.place(x=0, y=0)

pencere.mainloop()  