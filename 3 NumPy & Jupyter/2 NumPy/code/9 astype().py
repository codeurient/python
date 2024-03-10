import numpy as np

qutu = np.array(  [     [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]     ]  )


# astype() metodu array elementləri bir tipden basqa bir tipə cevirmek üçün istifadə olunur. 
# Məsələn, tam ədədlərdən ibarət arrayimiz varsa və onu kesir ededlere çevirmək lazımdırsa, bu 
# əməliyyatı yerinə yetirmək üçün astype() funksiyasından istifadə edə bilərik.
print(  qutu.astype(str)   )  
print(  qutu.astype(float)   )  