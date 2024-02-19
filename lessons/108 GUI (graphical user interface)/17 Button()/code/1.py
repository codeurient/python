
#! https://pypi.org/project/tkmacosx/    -  dokumentasiyada her sey movcuddur.

from tkinter import *

pencere = Tk()

# Button()    - bu klasdan duyme yaratmaq ucun istifade edilir

etiket = Button(
        pencere, 
        text="Duymeni bas!",
    )

etiket.pack()

pencere.mainloop()