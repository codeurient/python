# link() - hard link yəni, qatı link

# Bu metod fayllar ucun hard link yaratmaqda istifade edilir. Eger Esas yol silinerse
# hemin esas yol ucun yaradilmiw hard link oldugu kimi qalacaqdir. 

# link() metodunun symlink() metodundan ferqi ondan ibaretdir ki, link() metodu
# 1. sadece fayllar ucun istifade edilir
# 2. esas yol silinse bele link qalir
# 3. hard link sadece bir fayl ucun teyin edile biler

# symlink() metodu
# 1. hem fayllar hemde qovluqlar ucun istifade edilir
# 2. esas yol silindikde hemin yol ucun teyin edilmis link-de fealiyyetini itirir.
# 3. simvolik link birden cox fayllar ucun teyin edile biler

import os

yol = '/Users/proj/domains/PYTHON/test.txt'
hardLink = '/Users/proj/domains/PYTHON/test3.txt'

os.link(yol, hardLink)
