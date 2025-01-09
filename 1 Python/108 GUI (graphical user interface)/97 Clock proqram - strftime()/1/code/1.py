from tkinter import *
from time import *

#! 2) 
def vaxti_yenile():
    # strftime() - bu metod ile hal hazirki vaxti elde etmis olduq. saat:deqiqe:saniye.
    # python-nin resmi veb saytinda telimatlar ile tanis ola bilersiniz:
    #! https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
    vaxt_metni = strftime("%I:%M%:S")
    vaxt_etiketi.config(text=vaxt_metni)


#! 1) 
pencere = Tk()
vaxt_etiketi = Label(pencere, font=("Arial", 50), fg="#00FF00", bg="black")
vaxt_etiketi.pack()

vaxti_yenile()

pencere.mainloop()  