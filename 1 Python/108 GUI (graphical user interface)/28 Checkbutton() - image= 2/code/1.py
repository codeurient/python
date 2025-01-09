from tkinter import *
    
def goruntulemek():
    #! Muqayise etdikde 1 deyerini "YES" ile evez etmeyi unutmayin
    if(x.get() == "YES"):
        print("Raziliq verdin")
    else:
        print("Imtina etdin")

pencere = Tk()

# onvalue= ve offvalue= deyerlerine 1 ve 0 evezine Yes ve No yazmaq da olar.
# Yes ve No deyerlerini yazdiqda StringVar() metodundan istifade etmek lazimdir.
x = StringVar()

# image= parametrinden istifade ederek xana-nin yanina sekil elave etmekde mumkundur. 
sekil = PhotoImage(file='1 Python/108 GUI (graphical user interface)/28 Checkbutton() - image= 2/code/1.png')

xana = Checkbutton( pencere,                        
                    text="Men bununla raziyam",     
                    variable=x,                     
                    onvalue="YES",
                    offvalue="NO",
                    command=goruntulemek,
                    image=sekil,
                    compound='left',
                )

xana.pack()

pencere.mainloop()