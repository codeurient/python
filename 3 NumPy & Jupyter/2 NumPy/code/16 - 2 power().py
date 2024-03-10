import numpy as np

qutu1 = np.array(  [     [  [30, 40], [60, 20]  ]     ]  )

qutu2 = np.array(  [     [  [3]  ]     ]  )


# power() - bu metod ededin ustunu elde etmek ucun istifade edilir.

# Her deyer ucun ayri-ayri onun ustunu elde etmekde olar yaxud butun ededler ucun sadece 
# bir eded de teyin etmek olar

# 30 * 30 * 30  = 27000
# 40 * 40 * 40  = 64000
# 60 * 60 * 60  = 216000
# 20 * 20 * 20  = 8000

print(  np.power(qutu1, qutu2)   )       # [  [     [27000 64000]  [216000 8000]    ]  ]

# Bu cur yazilis qaydasida movcuddur.
print(  np.power(qutu1, 3)   )           # [  [     [27000 64000]  [216000 8000]    ]  ]