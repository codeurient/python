import numpy as np

qutu1 = np.array(  [     [30, 40, 60, 20, 10]     ]  )
qutu2 = np.array(  [     [30, 20, 10, 20, 20]     ]  )


# add() metodu toplama operatoru kimi iki ferqli array-in deyerlerini ayri ayri birbirleri ile cemlemek
# ucun istifade edilir. Yeni, bir array-in deyerleri diger array-in deyerlerinin uzerine elave edilir.
print(  np.add(qutu1, qutu2)   )       # [  [60 60 70 40 30]  ]