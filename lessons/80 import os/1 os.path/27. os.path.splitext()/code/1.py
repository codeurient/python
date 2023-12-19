# Bu metod faylin extension yeni uzantisi (elaveside deyilir) ile fayl adini 
# 2 hisse bolmek ucun istifade edilir.


import os

yol = '/Users/proj/domains/PYTHON/test.txt'

fayl, faylinUzantisi = os.path.splitext(yol)

print("Qovluq:", fayl)  
print("Faylin uzantisi:", faylinUzantisi)  