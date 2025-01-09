from tkinter import *

def gonder():
    print("Havanin temperaturu: " + str( skala.get() ) + " derecedir.")

pencere = Tk()

# 1) SEKIL elave edirik
istiSekil = PhotoImage(file='1 Python/108 GUI (graphical user interface)/40 Scale() - troughcolor=/code/isti.png')
istiEtiket = Label(image=istiSekil)
istiEtiket.pack()



#! troughcolor= parametri şkalada artıb-azalan hissənin rəngini təyin edir.
skala = Scale( pencere, from_=100, to=0, length=600, tickinterval=10, resolution=5, troughcolor='#69E', fg='#FF1', bg='#000')
skala.set(    ((skala['from']-skala['to']) / 2) + skala['to']    )
skala.pack()


# 2) SEKIL elave edirik
soyuqSekil = PhotoImage(file='1 Python/108 GUI (graphical user interface)/40 Scale() - troughcolor=/code/soyuq.png')
soyuqEtiket = Label(image=soyuqSekil)
soyuqEtiket.pack()


duyme = Button(pencere, text='Gonder', command=gonder, compound=LEFT)
duyme.pack()

pencere.mainloop()