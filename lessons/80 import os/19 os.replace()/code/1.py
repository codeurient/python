# replace() - bu metod movcud fayli yaxud qovlugu hal-hazirda oldugu yerden basqa yere dasimaq 
# ucun istifade edilir.

# qovluq1 yaradiriq ve hemin qovlugun icinde fayl yaxud basqa bir qovluq ola biler
# Asagidaki kodu işə saldiqda hemin qovluq yaxud fayl gonderilir qovluq2-ye

# Eger qovluq2 -nin icinde basqa fayl yaxud qovluq varsa onda xeta alasiyiq. Cunki evvelceden
# melumatlari hansi qovluga otureceyikse hemin qovlugun ici bos olmalidir. 

import os

yol1 = '/Users/proj/domains/PYTHON/qovluq1'
yol2 = '/Users/proj/domains/PYTHON/qovluq2'

os.replace(yol1, yol2)