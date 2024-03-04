# append() metodu arraylarin sonuna yeni deyer elave etmek ucun istifade edilir.

import numpy as np

#! 1ci parametr hansi array icine elave edileceyini bildirir.
#! 2ci array ise hansi deyerin elave edileceyini bildirir.
qutu1 = np.array(  [10, 20, 30, 40  ]  )
yeni_qutu1 = np.append(qutu1, 50)
print(   yeni_qutu1   )                         # [10 20 30 40 50]


#! Ic-ice array-lar olduqda hemin array-lar birlesir ve yeni deyer sona elave edilir.
qutu2 = np.array(  [   [10, 20], [30, 40]   ]  )
yeni_qutu2 = np.append(qutu2, 50)
print(   yeni_qutu2   )                         # [10 20 30 40 50]

#! Birden cox deyer elave etmek istedikde deyerler [] kvadrat moterize icinde yazilir.
qutu3 = np.array(  [   [10, 20], [30, 40]   ]  )
yeni_qutu3 = np.append(qutu3, [50, 60])
print(   yeni_qutu3   )                         # [10 20 30 40 50 60]