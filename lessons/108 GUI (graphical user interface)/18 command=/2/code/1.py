from tkinter import *
from tkmacosx import *

pencere = Tk()


def basmaq():
    print("Sen duymeni basdin")

# MAC sistemlərində "bg=" parametri cox vaxt islemir
    
# Bunun ucun terminalda "pip install tkmacosx" yazaraq MAC sistemine uygun olan versiyani qurasdirmaq lazimdir.
#! Versiyani qurasdirdiqdan sonra en yuxarida yazdigimiz kimi yazaraq "tkmacosx" modulunu import etmeliyik.
    
etiket = Button(
        pencere, 
        text="Duymeni bas!",
        command=basmaq,
        fg="#00FF00",
        bg="black",
    )
# Parametrler cox oldugu ucun hamisini yazmaq olmur ancaq islemeye qaydasini gorduz. Lazim olduqda 
# internetden diger parametrler haqqinda melumat ala bilersiz.

etiket.pack()

pencere.mainloop()