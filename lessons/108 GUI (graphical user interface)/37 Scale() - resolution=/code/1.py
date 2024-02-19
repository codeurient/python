from tkinter import *

pencere = Tk()

def gonder():
    print("Havanin temperaturu: " + str( skala.get() ) + " derecedir.")

# 1) resolution=     parametri ile şkalanın neçə-neçə qalxması gərəkdiyini təyin edirik.
skala = Scale( pencere, from_=100, to=0, length=600, orient=VERTICAL, tickinterval=10, resolution=5)
skala.pack()

duyme = Button(pencere, text='Gonder', command=gonder, compound=LEFT)
duyme.pack()

pencere.mainloop()