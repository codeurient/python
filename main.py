import numpy as np

qutu1 = np.array(  [     [  [30, 40], [60, 20]  ]     ]  )
qutu2 = np.array(  [     [  [30, 20], [10, 20]  ]     ]  )


# divide() - bu metod vurma emeliyyati icra edir

print(  qutu1 / qutu2             )       # [  [     [1. 2.] [6. 1.]    ]  ]
print(  np.divide(qutu1, qutu2)   )       # [  [     [1. 2.] [6. 1.]    ]  ]