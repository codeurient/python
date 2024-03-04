# cumprod() array elementlərinin məcmu hasilini hesablamaq üçün istifadə olunur.

import numpy as np

qutu1 = np.array(  [20, 40, 60, 70]  )

# 20 * 40 = 800
# 800 * 60 = 48000
# 48000 * 70 = 3360000
print(  np.cumprod(qutu1)  )                # [     20     800   48000 3360000]