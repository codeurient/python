from tkinter import *
from tkmacosx import *

pencere = Tk()

def basmaq():
    print("Sen duymeni basdin")

# Arxa fon qaradise duymeni basdiqda goy reng olur. 
# Duymenin basilmasina duymenin aktivlesmesi deyirler.
# Eger duymeni aktivlesdirdikde arxa fon rengi ve metn rengi oldugu kimi qalsin isteyirikse onda 
#! "activeforeground=" ve "activebackground=" parametrlerine "fg=" ve "bg=" parametrlerine verdiyimiz eyni rengleri vermek lazimdir.
etiket = Button(
        pencere, 
        text="Duymeni bas!",
        command=basmaq,
        fg="#00FF00",
        bg="#000",
        activeforeground="#00FF00",
        activebackground="#000",
    )

etiket.pack()

pencere.mainloop()