from tkinter import *

def gonder():
    print("Sifarisiniz:", siyahiQutusu.get(  siyahiQutusu.curselection()  ))

# 3) siyahiQutusu.size() - 1ci parametr ile hemise en son sayını əldə edirik.
#    sahe.get()          - 2ci parametr ile sahəyə daxil edilən dəyərləri əldə edirik.
def elaveEt():
    siyahiQutusu.insert(  siyahiQutusu.size(), sahe.get()  )
    # 4) Siyahiya yeni element elave edildikde qutunun ölçüsünün böyüməsi üçün yenidən belə yazırıq:
    siyahiQutusu.config(height=siyahiQutusu.size())

pencere = Tk()

siyahiQutusu = Listbox( pencere )
siyahiQutusu.pack()

siyahiQutusu.insert(  1, 'pizza'   )
siyahiQutusu.insert(  2, 'corek'   )
siyahiQutusu.insert(  3, 'sup'     )
siyahiQutusu.insert(  4, 'soyutma' )
siyahiQutusu.insert(  5, 'tike'    )

siyahiQutusu.config(height=siyahiQutusu.size())

# 1) Yeni elementler elave etmek ucun, yazi yazan sahe emele getiren Entry() klasindan istifade edirik. 
sahe = Entry()
sahe.pack()

gonder = Button(pencere, text='Gonder', command=gonder)
gonder.pack()

# 2) Sahede yazilan yeni elementleri Listbox()-a elave etmek ucun duyme yaradiriq. Duymeni basdiqda 
# isleyecek funksiyanin adi: "elaveEt" -dir. Hemin funksiyani yuxarida yazmisiq.
elaveEt = Button(pencere, text='Elave et', command=elaveEt)
elaveEt.pack()

pencere.mainloop()