# searchsorted() metodu çeşidlənmiş array icinde elementin yerini tapmaq üçün istifadə olunur


# Eger axtarilan deyer array icinde yoxdursa, onda bu deyeri hara qoymaq olarsa hemin deyerin 
# qoyulmasi mumkun ola bilecek indeksi qaytarir.

import numpy as np

qutu1 = np.array(  [1, 3, 5, 7, 9 ]  )
yeni_qutu1 = np.searchsorted(qutu1, 5)                               
print(  yeni_qutu1  )                       # 2


qutu2 = np.array(  [1, 3, 5, 7, 9 ]  )
yeni_qutu2 = np.searchsorted(qutu2, 10)                               
print(  yeni_qutu2  )                       # 10