# True & False

# True ile ust uste dusen deyerler qayitsin False ile ust-uste dusen qaytmasin demis oluruq burda.

import numpy as np

qutu1 = np.array(  [20, 30, 40, 50]  )

dy = [True, False, True, False]    

yeni_qutu1 = qutu1[dy]
print(  yeni_qutu1  )                       # [20 40]