from tkinter import *
def gonder():
    yemek = []
    #! 1) for dongusu ile seçilən elementlərin indekslərini əldə edirik. 0,1,3,4,5 və.s
    for index in siyahiQutusu.curselection():
        #! insert() metodu ilə həmin indeksə uyğun gələn elementi taparaq 'yemek' adlı list-ə əlavə edirik.
        yemek.insert(index, siyahiQutusu.get(index))
    #! 2) Sonra yenə for döngüsü ilə list-in içinə hansı elementlər yerləşdirmişiksə həmin elementləri çağırırıq.
    for elementler in yemek:
        print(elementler)
def elaveEt():
    siyahiQutusu.insert(  siyahiQutusu.size(), sahe.get()  )
    siyahiQutusu.config(height=siyahiQutusu.size())
def silmek():
    #! 3) secilen elementleri silmek ucun de 'for' dongusunden istifade edirik.
    #! Elementləri sildikdə onların indeksləri dəyişir. Buna görədə biz istəyən yox biz istəməyən element silinir. Bunun baş verməməsi üçün
    #! elementləri silməzdən əvvəl reversed() metodu ilə seçilən elementləri tərsinə sıralayaraq indeksi sonuncu indeks edirik və sondan silməyə 
    #! başlayırıq. 
    for index in reversed(  siyahiQutusu.curselection()  ):
        siyahiQutusu.delete(index)
    siyahiQutusu.config(height=siyahiQutusu.size())

pencere = Tk()
siyahiQutusu = Listbox( pencere, selectmode=MULTIPLE )
siyahiQutusu.pack()
siyahiQutusu.insert(  1, 'pizza'   )
siyahiQutusu.insert(  2, 'corek'   )
siyahiQutusu.insert(  3, 'sup'     )
siyahiQutusu.insert(  4, 'soyutma' )
siyahiQutusu.insert(  5, 'tike'    )

siyahiQutusu.config(height=siyahiQutusu.size())
sahe = Entry()
sahe.pack()

gonder = Button(pencere, text='Gonder', command=gonder)
gonder.pack()
elaveEt = Button(pencere, text='Elave et', command=elaveEt)
elaveEt.pack()
sil = Button(pencere, text='Sil', command=silmek)
sil.pack()
pencere.mainloop()