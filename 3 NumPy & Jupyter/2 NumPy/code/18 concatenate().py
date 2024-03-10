import numpy as np

qutu1 = np.array(  [  10, 20, 30  ]  )
qutu2 = np.array(  [  40, 50, 60  ]  )



# concatenate() - Bu metoddan ferqli array-lari bir-biri ile birlesdirmek ucun istifade edilir.

print(  np.concatenate([qutu1, qutu2])   )       # [10 20 30 40 50 60]