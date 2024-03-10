import numpy as np

qutu1 = np.array(  [     [  [30, 40], [60, 20]  ]     ]  )
qutu2 = np.array(  [     [  [3,   2], [1,   2]  ]     ]  )


# power() - bu metod ededin ustunu elde etmek ucun istifade edilir.
# 30 * 30 * 30  = 27000
# 40 * 40       = 1600
# 60            = 60
# 20 * 20       = 400

print(  np.power(qutu1, qutu2)   )       # [  [     [27000 1600]  [60 400]    ]  ]