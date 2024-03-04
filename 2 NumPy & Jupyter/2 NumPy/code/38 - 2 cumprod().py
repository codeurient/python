# cumprod() array elementlərinin məcmu hasilini hesablamaq üçün istifadə olunur.

import numpy as np

qutu1 = [100, 150, 199, 200, 250, 130]
qutu2 = [10, 50, 30, 40, 30, 10]

qiymet = np.array(qutu1)
miqdar = np.array(qutu2)

# 100 * 10 = 1000
# 150 * 50 = 7500
# 199 * 30 = 5970
# 200 * 40 = 8000
# 250 * 30 = 7500
# 130 * 10 = 1300
print(  np.cumprod([qiymet, miqdar], axis=0)  )      # [    [ 100  150  199  200  250  130] [1000 7500 5970 8000 7500 1300]    ]


yeni_array = np.cumprod([qiymet, miqdar], axis=0)   
print(yeni_array[1])                                 # [1000 7500 5970 8000 7500 1300]


toplam = np.cumprod([qiymet, miqdar], axis=0)   
print(  toplam[1].sum()  )                           # 31270