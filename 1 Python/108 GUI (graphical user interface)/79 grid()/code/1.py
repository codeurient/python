from tkinter import *
from tkinter import ttk

pencere = Tk()

basliqMetni = Label(pencere, text="Melumatlarinizi daxil edin", fg="red").grid(row=0, column=0, columnspan=2)

# grid() metodu ile elementleri setr ve xanalara ayiraraq ferqi-ferqli yerlerde yerlesdirmek mumkundur.
# row   - setr 
# colum - sutun 
etiketinBirinciAdi = Label(pencere, text="Birinci ad: ", width=10, fg="green").grid(row=1, column=0)
saheninBirinciAdi  = Entry(pencere).grid(row=1, column=1)

etiketinBirinciAdi = Label(pencere, text="Ikinci ad: ",  width=10, fg="green").grid(row=2, column=0)
saheninBirinciAdi  = Entry(pencere).grid(row=2, column=1)

etiketinBirinciAdi = Label(pencere, text="Email: ",      width=10, fg="green").grid(row=3, column=0)
saheninBirinciAdi  = Entry(pencere).grid(row=3, column=1)

# columnspan=2 - duymeni tam merkeze getirmek ucun 'columnspan' parametrinden istifade edilir.
# Normalda bizim iki sutunumuz (column) vardir. Bu iki sutunu birlesdirmek ucun 'columnspan=2' deyirik. 
gonderDuymesi = Button(pencere, text="Gonder").grid(row=4, column=0, columnspan=2)

pencere.mainloop()  