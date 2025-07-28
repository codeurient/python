# cumsum() array elementlərinin məcmu cəmini hesablamaq üçün istifadə olunur.

import numpy as np

qutu1 = np.array(  [20, 40, 60, 70]  )

# 20+40=60
# 60+60=120
# 120+70=190
print(  np.cumsum(qutu1)  )                 # [ 20  60 120 190]