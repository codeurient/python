import time
from tkinter import *
from tkinter.ttk import *

def basla():
    tapsiriq = 100
    x = 0
    while(x < tapsiriq):
        time.sleep(.03)
        yuklenmeZolagi['value'] += 1
        x += 1
        # 3) 'int()' metodu icinde 0-dan 100-e qeder artiran dustur yaziriq. 'round()' metodu ile ededi yuvarlaqlasdiririq. 'str()' metodu ile 
        # hemin ededi string tipine ceviririk. Final neticeni ise 'set()' metodu ile 'faiz' adli variable-in icine gonderirik.
        faiz.set(str(round(int((x/tapsiriq)*100))) + '%')
        # 4) Yuxarida yazdigimizi asagidaki kimide yazmaq olardi.
        metn.set(str(x) + '/' + str(tapsiriq) + " tapsiriq tamamlandi")
        #! pencere.update() yazdiqda ve proqrami sona catmadan qapatdiqda xeta aliriq:  
        #! update_idletasks - Bele bir xeta almamaq ucun ise bu metoddan istifade edirik. 
        pencere.update_idletasks()

pencere = Tk()

# 1) 'faiz' adinda variable yaradiriq. StringVar() metodu ile hemin variable-in 'string' tipli oldugunu deyirik. Bu variable-a yuxarida ki, 
# funksiya icinde deyer verdikden sonra, hemin variable-i asagida ki, 'Label()' klasinin 'textvariable=' parametrine gondereceyik. 
faiz = StringVar()

# 2) 'metn' adinda variable yaradiriq. StringVar() metodu ile hemin variable-in 'string' tipli oldugunu deyirik. Bu variable-a yuxarida ki, 
# funksiya icinde deyer verdikden sonra, hemin variable-i asagida ki, 'Label()' klasinin 'textvariable=' parametrine gondereceyik. 
metn = StringVar()

yuklenmeZolagi = Progressbar(pencere, orient=HORIZONTAL, length=300)
yuklenmeZolagi.pack(pady=20)

# 5) Yuxarida ki, neticeni Lable() klasi ile ekrana gonderirik
Label(pencere, textvariable=faiz).pack()

# 6) Yuxarida ki, neticeni Lable() klasi ile ekrana gonderirik
Label(pencere, textvariable=metn).pack()

duyme = Button(pencere, text="yuklenir", command=basla).pack()

pencere.mainloop()  