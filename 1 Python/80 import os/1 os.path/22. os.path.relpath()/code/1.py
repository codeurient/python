# relpath() - relative path yeni nisbi yol. Bu metod 2 parametr qebul edir.

# 1ci parametr tam yolu ifade edir. 2ci parametr ise elaqe qurmaq istediyimiz yoldur.

# Yeni, 'Users/DODI/Mac/QEBZ.mp4' bu yola getmek ucun 2 addim geri cixmaq lazimdir. Geri cixmaq 
# ucun ../ bele bir iwareden istifade edilir. Eger bu iwareden 2 dene olarsa ../../ bu o demekdir ki,
# 2 addim geri cix. Eger ../../../ 3 dene olarsa 3 addim geri cix ve.s

# Nece defe geri cixmaq lazim oldugunu bizim evezime proqram desin deye relpath() metodundan istifade edilir.
#  'Users/DODI/Mac/QEBZ.mp4' bu yola nisbeten 'Users/proj/domains/PYTHON/test.txt' bu yol ne qeder geri 
# cixmalidir ki, QEBZ.mp4 faylinin oldugu qovluga daxil ola bilek??? 
# relpath() metodu qeyd edir: ../../../proj/domains/PYTHON/test.txt  - bu qeder.

import os

esas_yol = 'Users/DODI/Mac/QEBZ.mp4'
cari_yol = 'Users/proj/domains/PYTHON/test.txt'

fayl_haqqinda = os.path.relpath(cari_yol, esas_yol)
print(  fayl_haqqinda  )

