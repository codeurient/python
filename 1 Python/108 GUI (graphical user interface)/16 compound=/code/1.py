from tkinter import *

pencere = Tk()

sekil = PhotoImage(file="1 Python/108 GUI (graphical user interface)/16 compound=/code/1.png")

# compound=    - mətn və şəkli necə və harda yerləşdirmək lazım onu təyin edir
# compound=left dedikdə, mətn sağ tərəfdə şəkil isə sol tərəfdə yerləşir.

etiket = Label(
    pencere, 
    text="GUI derslerimize xos gelmisiz", 
    font=('Arial', 40, 'bold'), 
    fg='#00FF00', 
    bg='#BBBFFF',
    relief=RAISED,
    bd=10,
    padx=10,
    pady=10,
    image=sekil,
    compound='left')

etiket.pack()

pencere.mainloop()