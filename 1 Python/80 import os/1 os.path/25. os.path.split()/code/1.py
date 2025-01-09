# Bu metod fayla gedən yolu iki hissəyə bölmək üçün 
# istifadə olunur: qovluq adı və fayl adı.


import os

yol = '/Users/proj/domains/PYTHON/test.txt'

qovluq, fayl = os.path.split(yol)

print("Qovluq:", qovluq)  
print("Faylin adi:", fayl)  