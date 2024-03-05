# median() metodu arraydaki dəyərlərin medianıni hesablamaq üçün istifadə olunur.


import numpy as np
#! Median ededlerin ardıcıl siyahısını iki bərabər yarıya bölən dəyərdir. Yeni deyerler ilk once
#! artan sira ile yeniden formalasir ve tam kerkezdeki deyer median sayilir.
qutu1 = [200, 300, 150, 130, 200, 280, 170]
yeni_array1 = np.array(qutu1)
# [130, 150, 170, 200, 200, 280, 300]
print(  np.median(yeni_array1)  )         # 200




#! Eger verilmis ededlerin sayi cutdurse, onda en ortada yerlesen ardicil iki eded toplanaraq 
#! 2-ye bolunur. 
qutu2 = [200, 300, 150, 130, 200, 280, 170, 188]
yeni_array2 = np.array(qutu2)
# [130, 150, 170, 188, 200, 200, 280, 300]   
print(  np.median(yeni_array2)  )         # (188 + 200) / 2 = 194.0