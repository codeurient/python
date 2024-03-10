# Eger her 2 yolda eyni fayli yaxud qovlugu isare edirse onda if eks halda else iwleyecekdir.

# Eger axtarilan fayl movcud deyildirse onda xeta mesaji alasiyiq.


import os

yol1 = '/Users/proj/domains/PYTHON/example.txt' 
yol2 = '/Users/proj/domains/PYTHON/test.txt' 

if os.path.samefile(yol1, yol2):
    print("Eyni fayl")
else:
    print("Ferqli fayl")