from tkinter import *

pencere = Tk()



# 1) Klaviaturada olan duymelere benzer duymeler elave etdik. Ancaq ekrani genislendirdikde W duymesi diger duymelerden ayrilir.
# Ne etmeliyik ki, ayrilmasin ve birlikde qalsin ? #! Frame() klasindan istifade ederek cercive yarada ve duymeleri hemin cerciveye qoya bilerik.
Button(pencere, text="W", font=("Consolas", 25), width=3).pack(side=TOP)
Button(pencere, text="A", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(pencere, text="S", font=("Consolas", 25), width=3).pack(side=LEFT)
Button(pencere, text="D", font=("Consolas", 25), width=3).pack(side=LEFT)

pencere.mainloop()  