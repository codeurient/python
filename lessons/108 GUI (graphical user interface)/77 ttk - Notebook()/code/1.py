from tkinter import *
# ttk standart tkinter vidcetlərindən daha muasir vidjetler teqdim eden moduldur. 
from tkinter import ttk

pencere = Tk()

# Notebook() ttk modulunun klasidir. Bu klasdan TAB-lar yaratmaq ucun istifade edilir. TAB-lar 1 pencere uzerinde ferqli 
# kecidler etmeye imkan veren alt pencerelerdir.
qeydKitabcasi = ttk.Notebook(pencere)

# Her tab ucun Frame() klasi ile cercive yaradiriq.
tab1 = Frame(qeydKitabcasi)
tab2 = Frame(qeydKitabcasi)

# add() metodu ile hemin yuxarida yaratmis oldugumuz hemin cerciveleri, pencereye elave edirik.
qeydKitabcasi.add(tab1, text="Tab 1")
qeydKitabcasi.add(tab2, text="Tab 2")
qeydKitabcasi.pack()

pencere.mainloop()  