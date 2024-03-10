# Muqayise operatoru

import numpy as np

qutu1 = np.array(  [20, 30, 40, 50]  )

operator1 = qutu1 > 35
yeni_qutu1 = qutu1[operator1]

print(  yeni_qutu1  )                       # [40 50]






qutu2 = np.array(  [2, 3, 4, 5]  )

operator2 = qutu2 % 2 == 0
yeni_qutu2 = qutu2[operator2]

print(  yeni_qutu2  )                       # [2 4]