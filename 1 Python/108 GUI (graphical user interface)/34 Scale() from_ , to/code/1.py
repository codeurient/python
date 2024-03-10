from tkinter import *

pencere = Tk()

# Scale() klasi ölçü təyin edən şkala yaradır.

# from_ şkalanın başlanğıcını təyin edir
# to    şkalanın sonunu təyin edir


# from_=100, to=0    - belede yazmaq olar.
skala = Scale(   
                    pencere,
                    from_=0,
                    to=100,
                )

skala.pack()

pencere.mainloop()