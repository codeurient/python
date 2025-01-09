# 1) os  -  emeliyyat sistemi ile iwlemek ucun istifade edilen moduldur. os modulunun metodlari emeliyyat
#  sistemini idare etmek, fayllara ve qovluqlara muraciet etmek ucun istifade edilir. 


# 2) ekranda bir fayl yaradiriq ve hemin faylin yolunu kopyalayiriq.

# 3) hemin yolu asagidaki kimi bir deyiskene gonderirik

# 4) 2 ters slesh simvolu yaziriq cunki diger simvollarin yaninda yazilan bir eded slesh hemin 
# simvollari string formatina cevirecekdir. Eks halda hemin simvol kodun bir hissesi kimi nezere 
# alina biler. Bunun olmamasi ucun hemin string formatina cevirmek istediyimiz simvolun yaninda 1 eded ters 
# slesh qoyuruq.

import os

path = "/Users/proj/domains/PYTHON/hereket.html"


# exists() - bu metod her hansisa bir faylin yaxud qovlugun var olub olmadigini yoxlayir.

# exists() - bu metod hemde teyin edilmis yolun her hansisa bir qovluga aid olub olmadigini yoxlayir.

if os.path.exists(path):
    print("Beli bele bir fayl movcuddur.")
else:
    print("Bele bir fayl movcud deyil.")