# cumprod() array elementlərinin məcmu hasilini hesablamaq üçün istifadə olunur.

import numpy as np

qutu1 = [100, 150, 199, 200, 250, 130]
qutu2 = [10, 50, 30, 40, 30, 10]

qiymet = np.array(qutu1)
miqdar = np.array(qutu2)

# 100 + 150 = 250
# 250 + 199 = 449
# 449 + 200 = 649
# 649 + 250 = 899
# 899 + 130 = 1029
# 1029 + 10 = 1039
# 1039 + 50 = 1089
# 1089 + 30 = 1119
# 1119 + 40 = 1159
# 1159 + 30 = 1189
# 1189 + 10 = 1199
print(  np.cumsum([qiymet, miqdar])  )      # [ 100  250  449  649  899 1029 1039 1089 1119 1159 1189 1199]