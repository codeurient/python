import numpy as np

qutu1 = np.array(  [     [  [30, 40], [60, 20]  ]     ]  )
qutu2 = np.array(  [     [  [30, 20], [10, 20]  ]     ]  )


# multiply() - bu metod vurma emeliyyati icra edir

print(  qutu1 * qutu2               )       # [  [     [900 800] [600 400]    ]  ]
print(  np.multiply(qutu1, qutu2)   )       # [  [     [900 800] [600 400]    ]  ]