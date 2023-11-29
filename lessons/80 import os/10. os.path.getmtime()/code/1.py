# Eger faylda (sadece fayl) her hansisa deyiwiklik edilerse getmtime() metodu hemin deyisikliyin
# edildiyi tarixi qaytaracaqdir.


import os
import time

faylin_yolu = '/Users/proj/domains/PYTHON/test.txt'

# Получение времени последнего доступа к файлу
giris_vaxti = os.path.getmtime(faylin_yolu)

saat_formatinda_elde_et = time.ctime(giris_vaxti) 

print(  saat_formatinda_elde_et  )