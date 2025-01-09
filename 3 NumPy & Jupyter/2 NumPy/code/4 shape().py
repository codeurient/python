import numpy as np

qutu = np.array(  [     [10, 20, 30, 40], [50, 60, 70, 80], [90, 100, 110, 120]     ]  )

# shape() metodu array-in uzunlugu haqqinda melumat elde etmek ucun istifa edilir.
# Yeni, array-in icinde neçə dənə element olduğunu öyrənmək üçün istifadə edilir.

# 1ci parameter: ic-ice olan elementlerin sayini bildirir.
# 2ci parameter: ayri-ayri array elementlerinin sayini bildirir.
print(  np.shape(qutu)  )  #! (3, 4)