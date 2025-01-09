from tkinter import *

pencere = Tk()

def gonder():
    print(f"Havanin temperaturu: {skala.get()}  derecedir.")

# 2) length= parametri ile şkalanın uzunluğunu təyin edirik.
# 3) orient= parametri ile şkalanı düzünə yaxud uzununa formalaşdırmaq mümkündür
skala = Scale( pencere, from_=100, to=0, length=600, orient=HORIZONTAL)
skala.pack()

# 1) Duymeni basdiqda Scale() klasinin deyerlerini elde eden funksiya yazdiq.
duyme = Button(pencere, text='Gonder', command=gonder, compound=LEFT)
duyme.pack()

pencere.mainloop()