from tkinter import *
from tkinter import ttk

pencere = Tk()

qeydKitabcasi = ttk.Notebook(pencere)

tab1 = Frame(qeydKitabcasi)
tab2 = Frame(qeydKitabcasi)

qeydKitabcasi.add(tab1, text="Tab 1")
qeydKitabcasi.add(tab2, text="Tab 2")
# 1) expand= - bu parametre True deyerini verdikde Qeyd Kitabcasi tam merekeze gelir
# 2) fill=   - bu parametre "both" deyerini verdikde Qeyd Kitabcasi pencerenin enini ve uzununu tam ehate edir
#              deyer olaraq: a) x       b) y      c) both     deyerlerini vermek olar.
qeydKitabcasi.pack(expand=True, fill="both")

Label(tab1, text="Salam, bu tab nomre 1-dir", width=50, height=25).pack()
Label(tab2, text="Salam, bu tab nomre 2-dir", width=50, height=25).pack()

pencere.mainloop()  