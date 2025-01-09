from tkinter import *

def birSeylerYaz(event):
    print( "Mouse koordinatlari: " + str(event.x) + "," + str(event.y) )

pencere = Tk()

# pencere.bind("<Button-1>",      birSeylerYaz)  # mouse-un sol duymesi
# pencere.bind("<Button-2>",      birSeylerYaz)  # surusdurme tekeri
# pencere.bind("<Button-3>",      birSeylerYaz)  # mouse-un sag duymesi
# pencere.bind("<ButtonRelease>", birSeylerYaz)  # mouse-u basdiqdan sonra buraxmaq
# pencere.bind("<Enter>",         birSeylerYaz)  # pencereye daxil olduqda
# pencere.bind("<Leave>",         birSeylerYaz)  # pencereni terk etdikde
pencere.bind("<Motion>",        birSeylerYaz)  # mouse hereket etdikde

pencere.mainloop()  