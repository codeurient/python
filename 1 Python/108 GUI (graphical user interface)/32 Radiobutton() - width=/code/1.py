from tkinter import *
    
yemekler = ['pizza', 'hotdog', 'doner']

pencere = Tk()

pizza = PhotoImage(file="1 Python/108 GUI (graphical user interface)/31 Radiobutton() - image=/code/pizza.png")
doner = PhotoImage(file="1 Python/108 GUI (graphical user interface)/31 Radiobutton() - image=/code/doner.png")
hotdog = PhotoImage(file="1 Python/108 GUI (graphical user interface)/31 Radiobutton() - image=/code/hotdog.png")

yemekSekilleri = [pizza, doner, hotdog]

x = IntVar()

# 'width=' beraber genislikde olmasi ucun width atributundan istifade edirik

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
                                width=275
                                
                            )

    yumruDuyme.pack(anchor=W)

pencere.mainloop()