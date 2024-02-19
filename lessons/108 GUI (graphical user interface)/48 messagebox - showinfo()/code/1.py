from tkinter import *
from tkinter import messagebox

# duymeni basdiqda funksiya islemeye baslayir ve ekrana xeberdarliq mesaji gosteren qutu cixir.

# hemin xeberdarliq mesaj qutusunu elde etmek ucun 'tkinter' kitabxanasinin 'messagebox' modulundan 
# istifade edirik. 
def klikle():
    # showinfo() - bu metod informasiya xarakterli mesaj gosterir.
    messagebox.showinfo()

pencere = Tk()

duyme = Button(pencere, command=klikle, text="Duymeni bas")
duyme.pack()

pencere.mainloop()