import numpy as np


qutu1 = np.array(  [  10, 20, 30, 40, 50, 60  ]  )

yeni_qutu = np.array_split(qutu1, 3)

print(yeni_qutu[1])     # [30 40]