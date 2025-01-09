# chmod() - eger birden cox istifadeci varsa hemin istifadecilerden kimler fayldan yaxud qovluqdan istifade
# ede biler, bildirmek ucun istifade edilir bu metodan. 

# Bu metod esas 3 parametr qebul edir: 
    # 1ci parametr - yol
    # 2ci parametr - UID
    # 3cu parametr - GID

# hal-hazirda emeliyyat sisteminde sadece bir istifadeci oldugu ucun numune gostere bilmirem.

# root Unix sisteminde esas istifadecidir ve onun UID-si 0 (sifir)-dir.

# Birden cox istifadeci olduqda ilk once hemin istifadecinin UID-sini oyrenirik ve 2ci parametrde yaziriq.

# 3cu parametri ise eger hemin fayli yaxud qovlugu bawqa qrupa aid etmek isteyirikse qeyd edirik. 

# Demeli, 1ci parametr yol, 2ci parametr hemin yolu aid etmek istediyimiz istifadeci, 3cu parametr ise
# hemin yolu aid etmek istediyimiz qrup.

import os

numune = '/Users/proj/domains/PYTHON/test.txt'

netice = os.chown(numune, 100, 2000)

print(netice)
