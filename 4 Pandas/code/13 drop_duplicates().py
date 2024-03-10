# drop_duplicates() funksiyası DataFrame-də dublikat (tekrarlanan) sətirləri silmək üçün istifadə olunur.

import pandas as pd

melumatlar = pd.read_csv('Datasets-main/company1.csv')

# eyni sutun eyni setr tekrarlanmadigi ucun hecneyi silmeyecek bu kod.
yeni_data = melumatlar.drop_duplicates()    
print(yeni_data)    


# Asagida ise 2 ferqli formada kod yazmisiq. 
# 1cisi sadece EEID sutununu silerek hemin sutun haqqinda olan melumati qaytarir
print(melumatlar['EEID'].drop_duplicates())
# 2cisi ise yene EEID sutununda tekrarlanan setri silerek cedvelin ozunu qaytarir. 
print(melumatlar.drop_duplicates('EEID')) 