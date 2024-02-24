import time
from tkinter import *
from tkinter.ttk import *

def basla():
    GB = 100
    yukle = 0
    suret = 1
    while(yukle < GB):
        time.sleep(.03)
        yuklenmeZolagi['value'] += (suret/GB) * 100
        yukle += suret
        faiz.set(str(round(int((yukle/GB)*100))) + '%')
        metn.set(str(yukle) + '/' + str(GB) + " GB tamamlandi")
        pencere.update_idletasks()

pencere = Tk()

faiz = StringVar()

metn = StringVar()

yuklenmeZolagi = Progressbar(pencere, orient=HORIZONTAL, length=300)
yuklenmeZolagi.pack(pady=20)

Label(pencere, textvariable=faiz).pack()

Label(pencere, textvariable=metn).pack()

duyme = Button(pencere, text="yuklenir", command=basla).pack()

pencere.mainloop()  