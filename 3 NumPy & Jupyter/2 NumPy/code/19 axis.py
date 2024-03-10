import numpy as np


qutu1 = np.array(  [  [10, 20], [30, 40]  ]  )
qutu2 = np.array(  [  [50, 60], [70, 80]  ]  )



#! axis parameteri demek olar ki, butun metodlar ucun teyin edile bilir.
#! axis parameteri default olaraq 0-dir (sifirdir). 

#? axis = 1 olduqda array deyerleri Y oxu istiqametinde emeliyyat icra edir.
print(  np.concatenate([qutu1, qutu2], axis = 1)   )   # [   [10 20 50 60] [30 40 70 80]   ]


#? axis = 0 olduqda array deyerleri X oxu istiqametinde emeliyyat icra edir.
print(  np.concatenate([qutu1, qutu2], axis = 0)   )   # [   [10 20]  [30 40]  [50 60]  [70 80]   ]