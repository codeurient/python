from tkinter import *

pencere = Tk()

# 4cu parametrde yaziriq: fg='green'
# 4cu parametrde yaziriq: fg='#00FF00'
etiket = Label(pencere, text="GUI derslerimize xos gelmisiz", font=('Arial', 40, 'bold'), fg='#00FF00')

etiket.pack()

pencere.mainloop()