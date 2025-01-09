# normcase() - bu meto emeliyyat sistemlerinde olan fayllarin yaxud qovluqlarin yol adlarini
# duzgun formaya salir. Yeni mesel ucn Users sozu bele yazilmalidirsa ve biz xeta ederek UsErS
# yazsaq onda hemin normcase() metodu bu xetani bawa duwerek onu normal hala salir.

# Bu metod WINDOWS emeliyyat sistemleri ucun kecerlidir.

# UNIX, MAC emeliyyat sistemlerinde hec bir deyiwiklik olmayacaq.


import os

faylin_yolu = 'UsErS/proj/domains/PYTHON/test.txt'

fayl_haqqinda = os.path.normcase(faylin_yolu)
print(  fayl_haqqinda  )