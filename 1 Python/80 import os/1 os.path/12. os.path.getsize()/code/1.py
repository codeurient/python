# getsize() - bu metod faylin olcusunu qaytarir. 

import os

faylin_yolu = '/Users/proj/domains/PYTHON/test.html'

fayl_haqqinda = os.path.getsize(faylin_yolu)

print(  fayl_haqqinda  )