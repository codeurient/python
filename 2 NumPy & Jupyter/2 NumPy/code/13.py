import numpy as np

qutu1 = np.array(  [     [  [30, 40], [60, 20]  ]     ]  )
qutu2 = np.array(  [     [  [30, 20], [10, 20]  ]     ]  )


# subtract() - bu metod add() metodunun tersidir. Yeni deyerleri bir-birinden cixaraq azaltmaq ucun 
# istifade edilir

print(  np.subtract(qutu1, qutu2)   )       # [  [     [0 20] [50 0]    ]  ]