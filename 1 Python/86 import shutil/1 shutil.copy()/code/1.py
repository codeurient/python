# copy() metodu copyfile() metodu ile eyni iwi gorur. Aradaki ferq nedir bes ?

# copyfile() metodu ile kopyalanan fayllarin meta melumatlari ve atributlari nezere alinmir.

# copy() metodu ile kopyalanan fayllarin meta melumatlari ve atributlari nezere alinir.

# Meta melumat ve atribut dedikde ne nezerde tutulur ? 

# 1. Faylin icinde olan mezmun, yazi
# 2. Hemin faylin r, w, a modunda olub olmamasi
# 3. Hemin faylin yaranma tarixi    - ctime() 
# 3. Hemin faylin yenilenme tarixi  - mtime() 
# 3. Hemin faylin açılma tarixi     - atime() 

import shutil

shutil.copy('example.txt', 'numune/copy.txt')