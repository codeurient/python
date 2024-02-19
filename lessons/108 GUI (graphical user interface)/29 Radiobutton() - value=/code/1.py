from tkinter import *
    
yemekler = ['pizza', 'hotdog', 'doner']

pencere = Tk()

x = IntVar()

# for-in dongusu ve range() metodu ile 0,1,2 indekslerini elde edirik. 
for index in range(len(yemekler)):
    # Eger 'value=index' yazmasaq, onda duymeni basdiqda butun yumru daireler eyni vaxtda secilecek.
    yumruDuyme = Radiobutton(   
                                pencere,
                                text=yemekler[index],
                                variable=x,
                                value=index
                            )

    yumruDuyme.pack()

pencere.mainloop()