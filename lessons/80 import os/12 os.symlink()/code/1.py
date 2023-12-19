# symbolic link yaratmaq ucun symlink() metodundan istifade ede bilerik. 

# Proqrami ise saldiqda yaradilan "yeniFayl.txt" fayli simvolik link olacaqdir

# symlink() metodu
# 1. hem fayllar hemde qovluqlar ucun istifade edilir
# 2. esas yol silindikde hemin yol ucun teyin edilmis link-de fealiyyetini itirir.
# 3. simvolik link birden cox fayllar ucun teyin edile biler

import os

faylin_yolu = '/Users/proj/domains/PYTHON/test.txt'
simvolikLink = '/Users/proj/domains/PYTHON/yeniFayl2.txt'

os.symlink(faylin_yolu, simvolikLink)







