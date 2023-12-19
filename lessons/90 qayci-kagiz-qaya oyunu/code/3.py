# Kodumuzu ise saldiqda birinci input() metodu bir melumat daxil etmeyimizi teleb edir.

# input() sahesine istenilen bir melumati daxil etdikden sonra, ekranda, print() metodu ile
# yazdirdigimiz diger melumatlar eks olunur. 

# choice() metodu onsuzda kodu işə saldigimizda ekrana random deyer yazdirmaq ucun 
# sirada gozluyurdu sadece input() metodu birinci islemeli idi ki, print() meotdu ile
# diger butun melumatlarin ekranda eks olundugnu gore bilek.

import random

secmek = ["qayci", "kagiz", "qaya"]

komputer = random.choice(secmek)

oyuncu = input("qayci, kagiz yoxsa qaya ?: ")

print("Komputer: ", komputer)
print("Oyuncu: ", oyuncu)