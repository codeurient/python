from tkinter import *

def gonder():
    # 5) sahede yazilan mezmunu elde etmek ucun get() metodundan istifade edirik ve elde etdiyimiz deyeri "ad" variable-ina gonderirik.
    ad = qeyd.get()
    print("salam: " + ad)
   
def silmek():
    # 7) delete() metodunun içində 2 parametr yaziriq: 1ci parametr baslangici teyin edir. Yəni 0.  2ci parametr isə sonu təyin edir. 
    # Yəni END. Sonunun nə qədər uzun olacağını bilmədiyimiz üçün END yazdıq ki avtomatik olaraq sonu həmişə özü təyin etsin. 
    #! 0 (sifir) yeni baslangic ile End yeni son arasinda ne qeder simvol varsa, hamisini SIL.
    qeyd.delete(0, END)

def tekTekSilmek():
    # 9) len() uzunluq verir. Indekslenme ise 0-dan baslayir. Hemise en sonuncu simvolun indeksini elde etmek ucun ÇIX BİR yazmışıq. 
    # Məsələn: salam sözü 5 simvolludur. m hərfinin indeksi ise 4-dür. Əgər çıx 1 yazmasaq len() metodu 5 verecek, ancaq 5ci indeks 
    # olmadığı üçün heçnə əldə etmiyəsiyik. Çünki s-0, a-1, l-2, a-3, m-4 dür. Çıx bir dedikdə həmişə ən sonuncu indeksi əldə edirik.
    # delete() metodu isə ən sonuncu indeksdən END-ə qədər hər şeyi silir. Ən sonuncu indeksdə həmişə birdənə olduğu üçün, simvollar tək-tək silinir.
    qeyd.delete(len(qeyd.get())-1, END)
    
pencere = Tk()

# 1) Yazi yazmaq ucun sahe yaradiriq.
qeyd = Entry( pencere, font=('Arial', 30) )
# 2) Hemin yazi yazmaq ucun olan saheni sol terefe yerlesdiririk.
qeyd.pack(side=LEFT)

# 3) Sahede yazilan yazini gondermek ucun duyme yaradirik
#? Bu duymeni basdiqda, sahede yazilan yazini gondermesi ucun funksiya lazimdir.
#? Hemin funksiyanin adi "command=" parametrinde qeyd etdiyimiz "gonder" -dir.
gonderen_duyme = Button( pencere, text="Gonder", command=gonder )
# 4) Sahede yazilan yazini gondermek ucun olan duymeni sag terefe yerlesdiririk.
gonderen_duyme.pack(side=RIGHT)

# 6) silmek ucun olan duymeni yaradiriq. Silme isini gorecek funksiyani yuxarda yaziriq. Hemin funksiyanin adı "silmek" olacaq
silen_duyme = Button( pencere, text="Sil", command=silmek )
silen_duyme.pack(side=RIGHT)

# 8) silmek ucun olan duymeni yaradiriq. Silme isini gorecek funksiyani yuxarda yaziriq. Hemin funksiyanin adı "silmek" olacaq
tekTekSilen_duyme = Button( pencere, text="Tek-tek sil", command=tekTekSilmek )
tekTekSilen_duyme.pack(side=RIGHT)

pencere.mainloop()