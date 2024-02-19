from tkinter import *
    
def goruntulemek():
    if(x.get() == 1):
        print("Raziliq verdin")
    else:
        print("Imtina etdin")

pencere = Tk()

# onvalue= ve offvalue= deyerlerine 1 ve 0 evezine True ve False yazmaq da olar.
# True ve False deyer yazdiqda IntVar() metodu evezine BooleanVar() metodunu yazmaq lazimdir.
x = BooleanVar()

# image= parametrinden istifade ederek xana-nin yanina sekil elave etmekde mumkundur. 
sekil = PhotoImage(file='lessons/108 GUI (graphical user interface)/27 Checkbutton() - image=/code/1.png')

xana = Checkbutton( pencere, 
                    text="Men bununla raziyam", 
                    variable=x,
                    onvalue=True,
                    offvalue=False,
                    command=goruntulemek,
                    image=sekil,
                    compound='left',
                )

xana.pack()

pencere.mainloop()