
#! hstack() metodu array deyerlerini Y oxu istiqametinde birlesdirmek ucun istifaed edilir.
import numpy as np


qutu1 = np.array(  [  [10, 20], [30, 40]  ]  )
qutu2 = np.array(  [  [50, 60], [70, 80]  ]  )


#? axis = 1 olduqda array deyerleri Y oxu istiqametinde emeliyyat icra edir.
print(  np.concatenate([qutu1, qutu2], axis = 1)   )   # [   [10 20 50 60] [30 40 70 80]   ]


#? hstack() metodu concatenate() metodunun axis parametri 1 olduqda gorduyu isi gorur.
print(  np.hstack([qutu1, qutu2])   )                  # [   [10 20 50 60] [30 40 70 80]   ]