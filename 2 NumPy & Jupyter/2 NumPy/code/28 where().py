# where() metodu şərt qoşaraq, array elementlərinin indekslərini tapmaq üçün istifadə olunur.

import numpy as np

qutu1 = np.array(  [3, 4, 1, 7, 8 ]  )
yeni_qutu1 = np.where(qutu1 == 4)                               
print(  yeni_qutu1  )                       # (array([1]),)



qutu2 = np.array(  [3, 4, 1, 7, 8 ]  )
yeni_qutu2 = np.where(qutu2 % 2 == 0)                                  
print(  yeni_qutu2  )                       # (array([1, 4]),)