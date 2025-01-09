# walk() - bu metod gosterilen yolda ne qeder qovluq varsa hemin qovluqlarin adlarini
# o qovluqlarda olan alt qovluqlarin adlarini her qovluqda ve alt qovluqda olan fayllarin 
# adlarini elde etmek ucun istifade edilir.

import os

yol = '/Users/proj/domains/PYTHON'

for root, dirs, files in os.walk(yol):
    print(f'Kataloq: {root}')
    print(f'Alt kataloq: {dirs}')
    print(f'Fayllar: {files}')