# Burda input() sahesine ne geldi yox sadece lazim olan 3 deyerden birini yaza bilmemiz ucun 
# while konstruksiyasindan istifade edirik. 

import random

secmek = ["qayci", "kagiz", "qaya"]
komputer = random.choice(secmek)

# Yeni, ne qeder ki axtardigimiz deyer secmek variable-inin icinde yoxdu deye sorgu yaradiriq.
# Ilk once 'oyuncu' adinda variable yaradiriq ve baslangic deyer olaraq "None" veririk.
oyuncu = None
while oyuncu not in secmek:
    oyuncu = input("qayci, kagiz yoxsa qaya ?: ")

print("Komputer: ", komputer)
print("Oyuncu: ", oyuncu)