# listdir() - bu metod teyin edilmis yolda hansi fayl ve qovluqlarin oldugunu gostermek
# ucun istifade edilir.

import os

yol = '/Users/proj/domains/PYTHON'

linkSiyahisi = os.listdir(yol)

for melumatlar in linkSiyahisi:
    print(melumatlar)