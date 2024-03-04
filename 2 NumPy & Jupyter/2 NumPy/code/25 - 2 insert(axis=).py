import numpy as np

#! axis parametrinden istifade etdikde ve deyer olaraq axis=1 dedikde, 50 deyeri, indeks-i 0 olan alt array-in 
#! icindeki 1 indeksine elave edilir. 60 deyeri ise indeksi 1 olan alt-array-in icindeki 1 indeksine elave edilir.
qutu1 = np.array(  [   [10, 20], [30, 40]   ]  )
yeni_qutu1 = np.insert(qutu1, 1, [50, 60], axis=1)
print("1) ",   yeni_qutu1   )                         # [   [10 50 20]  [30 60 40]   ]



#! axis parameterinden istifade etdikde ve deyer olaraq axis=0 dedikde, [50, 60] array-i elave edilir, 
#! qutu2 arrayinin icerisine alt-array olaraq.  
qutu2 = np.array(  [   [10, 20], [30, 40]   ]  )
yeni_qutu2 = np.insert(qutu2, 1, [50, 60], axis=0)
print("2) ",   yeni_qutu2   )                         # [   [10 20] [50 60] [30 40]   ]



#! axis parameterinden istifade etdikde ve deyer olaraq axis=1 dedikde, tek olan 50 deyeri array-in hem 
#! 1ci hem 2ci alt alt-array-larina ayri-ayri elave edilir.
qutu3 = np.array(  [   [10, 20], [30, 40]   ]  )
yeni_qutu3 = np.insert(qutu3, 1, 50, axis=1)
print("3) ",   yeni_qutu3   )                         # [   [10 50 20]  [30 50 40]   ]



#! axis parameterinden istifade etdikde ve deyer olaraq axis=0 dedikde, proqram, array-in 1ci ve 2ci alt 
#! array-larini ayri-ayri deyer kimi qebul edir. 1ci array-in indeksi 0, 2ci array-in indeksi 1-dir.
#! 50 deyeri ise indeksi 1 olan alt-array-in yerine elave edilir. 2ci alt-array-in indeksi ise 2 olur. 
qutu4 = np.array(  [   [10, 20], [30, 40]   ]  )
yeni_qutu4 = np.insert(qutu4, 1, 50, axis=0)
print("4) ",   yeni_qutu4   )                         # [   [10 20]   [50 50]   [30 40]   ]



#! insert() metodunun 2ci parametrinde [] kvadrat moterize icerisinde birden cox deyer yazaraq ferqli
#! indekslere yeni array deyerleri elave ede bilerik. 
qutu5 = np.array(  [   [10, 20], [30, 40]   ]  )
yeni_qutu5 = np.insert(qutu5, [1, 2], 50, axis=0)
print("5) ",   yeni_qutu5   )                         # [   [10 20]   [50 50]   [30 40]   [50 50]   ]