# symbolic link yaratmaq ucun symlink() metodundan istifade ede bilerik. 

# Yeni yaradilan "yeniFayl.txt" fayili simvolik link olacaqdir ve bunun ucun 
# islink() metodu TRUE qaytarir.

import os

faylin_yolu = '/Users/proj/domains/PYTHON/abc.txt'

os.symlink(faylin_yolu, 'yeniABC.txt')

yeni_simvolik_link = '/Users/proj/domains/PYTHON/yeniABC.txt'

fayl_haqqinda = os.path.islink(yeni_simvolik_link)

print(  fayl_haqqinda  )




