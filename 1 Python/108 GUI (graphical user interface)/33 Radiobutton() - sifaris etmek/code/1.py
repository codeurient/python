from tkinter import *
yemekler = ['pizza', 'hotdog', 'doner']

def sifaris():
    if(x.get() == 0):
        print("Pizza sifaris etdiniz")
    elif(x.get() == 1):
        print("Hotdog sifaris etdiniz")
    elif(x.get() == 2):
        print("Doner sifaris etdiniz")
    else:
        print("Ne yemek isteyirsiniz?")

pencere = Tk()

pizza = PhotoImage(file="1 Python/108 GUI (graphical user interface)/31 Radiobutton() - image=/code/pizza.png")
doner = PhotoImage(file="1 Python/108 GUI (graphical user interface)/31 Radiobutton() - image=/code/doner.png")
hotdog = PhotoImage(file="1 Python/108 GUI (graphical user interface)/31 Radiobutton() - image=/code/hotdog.png")

yemekSekilleri = [pizza, doner, hotdog]
x = IntVar()

for index in range(len(yemekler)):
    yumruDuyme = Radiobutton(   
                                pencere,
                                text=yemekler[index],
                                variable=x,
                                value=index,
                                image=yemekSekilleri[index],
                                compound=LEFT,
                                font=('Impact', 50),
                                padx=25,
                                pady=25,
                                indicatoron=0,
                                width=275,
                                command=sifaris
                            )
    yumruDuyme.pack(anchor=W)
pencere.mainloop()