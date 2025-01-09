# isfile() - bu metod yolun qovluq olub olmadigini teyin edir.


import os

# faylin_yolu = '/Users/proj/domains/PYTHON/test.html'
faylin_yolu = '/Users/proj/domains/PYTHON'

fayl_haqqinda = os.path.isdir(faylin_yolu)

print(  fayl_haqqinda  )