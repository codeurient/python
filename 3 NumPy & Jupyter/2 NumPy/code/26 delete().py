# delete() metodu array ve alt-array-larin icerisinden deyer silmek ucun istifade edilir. Silmek ucun delete() 
# metodunun ikinci parametrinde silinecek array deyerinin, yaxud alt-array-in indeksini yazmaq lazimdir.

import numpy as np

qutu1 = np.array(  [10, 20, 30, 40  ]  )
yeni_qutu1 = np.delete(qutu1, 1)
print('1) ',   yeni_qutu1   )                         # [10 30 40]


#! 2 eded alt array olarsa ve delete() metodunun ikinci parametrinde sadece 1 yazarsaq, ilk once alt array-lar
#! birlesir sonra ise 1ci indekse uygun gelen deyer hansi olarsa hemin deyer silinir. 
qutu2 = np.array(  [    [10, 20],   [30, 40]   ]  )
yeni_qutu2 = np.delete(qutu2, 1)
print('2) ',   yeni_qutu2   )                         # [10 30 40]


#! 2 eded alt array olarsa ve delete() metodunun ikinci parametrinde sadece 1 yazarsaq, ilk once alt array-lar
#! birlesir sonra ise 1ci indekse uygun gelen deyer hansi olarsa hemin deyer silinir. 
qutu3 = np.array(  [    [10, 20],   [30, 40], [50, 60]   ]  )
yeni_qutu3 = np.delete(qutu3, 1)
print('3) ',   yeni_qutu3   )                         # [10 30 40 50 60]


#! axis=1 yazdiqda, ayri-ayri her alt-array icerisinde indeksi 1 olan deyere muraciet ederek, delete()
#! metodu ile hemin deyeri silirik. 
qutu4 = np.array(  [    [10, 20],   [30, 40],   [50, 60]   ]  )
yeni_qutu4 = np.delete(qutu4, 1, axis=1)
print('4) ',   yeni_qutu4   )                         # [    [10]   [30]   [50]     ]


#! axis=0 yazdiqda, ayri-ayri her alt-array-in ozunu nezerde tutmus oluruq, icini yox. 
#! 0 - [10, 20]
#! 1 - [30, 40]
#! 2 - [50, 60]
qutu5 = np.array(  [    [10, 20],   [30, 40],   [50, 60]   ]  )
yeni_qutu5 = np.delete(qutu5, 1, axis=0)
print('5) ',   yeni_qutu5   )                         # [     [10 20]   [50 60]     ]