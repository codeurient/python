from tkinter import *
    
yemekler = ['pizza', 'hotdog', 'doner']

pencere = Tk()

x = IntVar()

for index in range(len(yemekler)):
    yumruDuyme = Radiobutton(   
                                pencere,
                                text=yemekler[index],
                                variable=x,
                                value=index
                            )

    # yumru duymeler ve yazilar bir duz boyunca siralanmadiqlari ucun seliqesiz gorsenirler
    # seliqeli formada siralamaq ucun pack() metoduna anchor= parametrini vermek lazimdir. 
    yumruDuyme.pack(anchor=W)

pencere.mainloop()