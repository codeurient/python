
#! vstack() metodu array deyerlerini X oxu istiqametinde birlesdirmek ucun istifaed edilir.
import numpy as np


qutu1 = np.array(  [  [10, 20], [30, 40]  ]  )
qutu2 = np.array(  [  [50, 60], [70, 80]  ]  )


#? axis = 0 olduqda array deyerleri X oxu istiqametinde emeliyyat icra edir.
print(  np.concatenate([qutu1, qutu2], axis = 0)   )   # [  [10 20] [30 40] [50 60] [70 80]  ]


#? hstack() metodu concatenate() metodunun axis parametri 0 olduqda gorduyu isi gorur.
print(  np.vstack([qutu1, qutu2])   )                  # [  [10 20] [30 40] [50 60] [70 80]  ]