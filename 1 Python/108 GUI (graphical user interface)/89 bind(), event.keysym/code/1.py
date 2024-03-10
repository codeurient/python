from tkinter import *

#! 2)
# Duymeni basdiqda event hemin funksiyanin 'event' parametrine oturulur. 
def birSeylerYaz(event):
    #! 3)
    # keysym -  event obyektinin atributudur. Basilan duymenin simvolunu elde etmek ucun istifade edilir.
    vidjet.config(text=event.keysym)

pencere = Tk()

#! 1) 
# bind() - bu metod funksiya ile event arasinda elaqe yaratmaq ucun istifade edilir.
# 1ci parametr event-dir. <Key> - yeni klavyaturada ki, her hansisa duymeni nezerde tutur. 
# 2i parametri hemin event bas verdikde isleyecek funksiyadir.

# <Button-1> - mausun sol duymesini basmaq event-idir.
# <Control-c> - Ctrl + c duymelerini basmaq event-idir. ve.s
pencere.bind("<Key>", birSeylerYaz)

vidjet = Label(pencere, font=("Helvetica", 100), width=5, height=2)
vidjet.pack()

pencere.mainloop()  