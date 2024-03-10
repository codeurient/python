from tkinter import *

pencere = Tk()

def gonder():
    print("Havanin temperaturu: " + str( skala.get() ) + " derecedir.")

skala = Scale( pencere, from_=100, to=0, length=600, orient=VERTICAL, tickinterval=10, resolution=5)
#! 1) set() -  metodu ile şkalanın başlanğıcda dəyəri nə olsun təyin edirik.
# Gosterici 1000 ile 0 arasinda olarsa ve biz proqramı işə saldıqda şkalanın göstəricisinin həmişə tam mərkəzdən 
# başlamasını istəyiriksə necə edəcəyik ? Çünki hər dəfə şkalanın göstəricisi fərqli olduqda set() metodu içində 
# əl ilə manual dəyişmək iki iş görmək olacaqdır. Bunun üçün set() metodu içində düstur yazmaq lazımdır ki, avtomatik 
# olaraq həmin mərkəzi proqram özü, düstur vasitəsi ilə təyin etsin
skala.set(50)
skala.pack()

duyme = Button(pencere, text='Gonder', command=gonder, compound=LEFT)
duyme.pack()

pencere.mainloop()