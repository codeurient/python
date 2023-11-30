# symbolic linki silmek ucun unlink() metodundan istifade edilir.

# unlink() metodunu istifade etmek ucun Path modulunu import etmek lazimdir.

# Sonra ise yolu Path() funksiyasinin icinde yaziriq ve simvolik linki unlink() metodu ile silirik.

import os

from pathlib import Path

faylin_yolu = Path('/Users/proj/domains/PYTHON/test.html')


yeni_simvolik_link = Path('/Users/proj/domains/PYTHON/yeniFayl.txt')
yeni_simvolik_link.unlink()

fayl_haqqinda = os.path.islink(yeni_simvolik_link)
print(  fayl_haqqinda  )