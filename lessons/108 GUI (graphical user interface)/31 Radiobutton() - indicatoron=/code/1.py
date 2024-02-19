from tkinter import *
    
yemekler = ['pizza', 'hotdog', 'doner']

pencere = Tk()

pizza = PhotoImage(file="lessons/108 GUI (graphical user interface)/31 Radiobutton() - image=/code/pizza.png")
doner = PhotoImage(file="lessons/108 GUI (graphical user interface)/31 Radiobutton() - image=/code/doner.png")
hotdog = PhotoImage(file="lessons/108 GUI (graphical user interface)/31 Radiobutton() - image=/code/hotdog.png")

yemekSekilleri = [pizza, doner, hotdog]

x = IntVar()
# 'yumru daire' yaxud 'kvadrat' seçicilər görsənsin mi yoxsa görsənməsin mi ?  
# Eger 'yumru daire' yaxud 'kvadrat' seciciler gorsenmesin isteyirikse onda 'indicatoron=' atributuna 0 (sifir) veririk
# Eger 'yumru daire' yaxud 'kvadrat' seciciler gorsensin isteyirikse onda 'indicatoron=' atributuna 1 (bir) veririk

#! 'indicatoron=' atributu 0 (sifir) oldukda sekil ve metn butov bir qutu icine qoyulur ve hemin qutu seçilən olur.

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
                                indicatoron=0
                            )

    yumruDuyme.pack(anchor=W)

pencere.mainloop()