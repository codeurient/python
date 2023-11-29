# Eger qovluqda her hansisa deyiwiklik edilerse getctime() metodu hemin deyisikliyin
# edildiyi tarixi qaytaracaqdir.

# Faylda edilen deyisiklikde buna tesir edir. Yeni faylin yolunu gostermek serti ile
# eger faylin icinde bir deyisiklik edilerse onda hemin deyisikliyin edildiyi tarix qayidacaqdir.
#! faylin_yolu = '/Users/proj/domains/PYTHON/text.txt'

# Eger meselen ucun, fayli hemin qovluq icinden goturub basqa qovluga qoysaq onda qovluqda
# deyisiklik etmis hesab edilecekdir ve hemin deyisikliyin tarixi ekrana yazdirilacaqdir.
#! faylin_yolu = '/Users/proj/domains/PYTHON'


import os
import time

faylin_yolu = '/Users/proj/domains/PYTHON'

giris_vaxti = os.path.getctime(faylin_yolu)

saat_formatinda_elde_et = time.ctime(giris_vaxti) 

print(  saat_formatinda_elde_et  )