# sort() metodu array-daki elementləri çeşidləmək üçün istifadə olunur
# Bu ve diger her metod ferqli emeliyyatlar icra edirler. Hamisini yazmaq mumkun olmur.
# Bir metodun isleme qaydasini bildikde arasdirma ve praktika ederek, ferqli neticeler elde etmek olur.

import numpy as np


qutu1 = np.array(  [7, 8, 4, 12, 9]  )
print( np.sort(qutu1) )                         # [ 4  7  8  9 12]


qutu2 = np.array(  [[7, 8, 4, 12, 9], [2, 8, 5, 1, 3]]  )
print( np.sort(qutu2) )                         # [  [ 4  7  8  9 12]  [ 1  2  3  5  8]  ]




































# qutu3 = np.array([7, 8, 4, 12, 9])
# np.sort(qutu3)  
# print(qutu3)                                    # netice eyni: [ 7  8  4 12  9]


# qutu4 = np.array([[7, 8, 4, 12, 9], [2, 8, 5, 1, 3]])
# yeni_qutu4 = np.sort(qutu4)[::-1]
# print(yeni_qutu4)                               # [5 4 3 2 1]


# qutu5 = np.array([3, 1, 2, 5, 4])
# qutu5.sort(kind='mergesort')
# print(qutu5)                                    # [1 2 3 4 5]


# qutu6 = np.array([3, 1, 2, 5, 4])
# qutu6.sort(kind='quicksort')
# print(qutu6)                                    # [1 2 3 4 5]



# qutu7 = np.array([3, 1, 2, 5, 4])
# print(qutu7.sort(kind='mergesort'))             # None



