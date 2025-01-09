# insert() metodu göstərilən array mövqeyinə yeni bir dəyər daxil edir.

import numpy as np

#! 1ci parametr hansi array icinde elave edilsin onu bildirir.
#! 2ci parametr hemin array-in hansi indeksine elave edilsin bildirir
#! 3cu parametr hemin indekse hansi deyerin elave edileceyini bildirir.
qutu1 = np.array(  [10, 20, 30, 40  ]  )
yeni_qutu1 = np.insert(qutu1, 1, 50)
print("1) ",   yeni_qutu1   )                         # [10 50 20 30 40]



#! Ic-ice array-lar birlesdirilir sonra göstərilən array (qutu2) mövqeyinə yeni bir dəyər daxil edilir.
qutu2 = np.array(  [   [10, 20], [30, 40]   ]  )
yeni_qutu2 = np.insert(qutu2, 1, 50)
print("2) ",   yeni_qutu2   )                         # [10 50 20 30 40]



#! Birden cox deyer elave etmek istedikde [] kvadrat moterizeden istifade edilir. Yene, ic-ice array-lar 
#! birlesdirilir ve hemin 2 deyer elave edilir birlesdirilen qutu5 arra-ina 
qutu3 = np.array(  [   [10, 20], [30, 40]   ]  )
yeni_qutu3 = np.insert(qutu3, 1, [50, 60])
print("5) ",   yeni_qutu3   )                         # [10 50 60 20 30 40]

